'''
This work is licensed under CC BY-NC-SA 4.0 

Adapted from https://github.com/phoenix104104/fast_blind_video_consistency/blob/master/evaluate_WarpError.py
By Yingshu Chen

This script evaluates both warpping MSE and warpping LPIPS with occulsion masks

CUDA_VISIBLE_DEVICES=0 python evaluate_temporal_consistency.py \
--data_dir ../results/chair_14/test_renders_path_blackbg \
--flow_dir ../results/nerf_synthetic/chair/optical_flow 
'''

import sys
sys.path.append('core')

import argparse
import os
import cv2
import glob
from PIL import Image
import time
import numpy as np
import torch

# import datasets
from utils import flow_viz
from utils import frame_utils
from raft import RAFT
from utils.utils import InputPadder, forward_interpolate, warp
from tqdm import tqdm
import lpips
from datetime import datetime

def load_image(imfile, resize=1024, device='cuda', mode="RGB"):
    img = Image.open(imfile).convert(mode)
    w,h = img.size
    if (w >= h) and (w > resize):
        new_w = resize
        new_h = int(1.0 * new_w / w * h)
        img = img.resize((new_w, new_h))
    elif (h > w) and (h > resize):
        new_h = resize
        new_w = int(1.0 * new_h / h * w)
        img = img.resize((new_w, new_h))

    img = np.array(img).astype(np.float32) / 255.0
    if img.ndim == 3:
        img = torch.from_numpy(img).permute(2, 0, 1)
    else:
        img = torch.from_numpy(img)
    return img[None].to(device)

def sort_key(x):
    x = os.path.basename(x)
    if len(x) > 2 and x[0]=='r' and x[1] == '_': #syn
        return int(x[2:].split(".")[0])
    elif len(x) > 2 and x[1] == '_': #nsvf
        return x[2:]
    else:
        return x

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='temporal consistency evaluation')

    parser.add_argument('--data_dir', type=str,  default='data/scene/path',   help='path to data folder')
    parser.add_argument('--flow_dir', type=str,  default='data/scene/optical_flow',   help='path to estimated optical flow folder')
    parser.add_argument('--style',  type=int, help='style id')
    parser.add_argument('--intervals', default="1,10", help='short/long range, 1 or 10, 3 for synthetic data')
    # parser.add_argument('--intervals', nargs="+", type=int, default=[1,10])
    parser.add_argument('--max_side', type=int, default=1024, help='maximum image side')

    args = parser.parse_args()
    print(args)

    device = torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")    

    # load sequence frame paths
    exts = ['.png', '.jpg', '.jpeg', '.exr']
    frame_names = os.listdir(args.data_dir)
    frames =sorted([os.path.join(args.data_dir, x) for x in frame_names if not x.startswith('.') and any((x.lower().endswith(ext) for ext in exts))], key=sort_key)
    frame_names = [os.path.basename(x).split(".")[0] for x in frames]
    print("Evaluating %d frames"%len(frames))


    ## Initializing LPIPS model
    # loss_fn_alex = lpips.LPIPS(net='alex').to(device) # best forward scores
    loss_fn_alex = lpips.LPIPS(net='alex', spatial=True).to(device) # best forward scores, set spatial=True to get original results for later masking again
    # loss_fn_vgg = lpips.LPIPS(net='vgg') # closer to "traditional" perceptual loss, when used for optimization

    # Create output file, save result in optical flow folder
    metric_file = os.path.join(args.flow_dir, "WarpError.txt")
    with open(metric_file, "a") as f:
        f.write("*********************\n")
        f.write("evaluate %s\n"%args.data_dir)
        f.write(str(datetime.now()))
        if args.style is not None:
            f.write(" - Style ID: %d"%args.style)
        f.write("\n")
    

    ### Start evaluation
    # different ranges
    intervals = list(args.intervals.split(","))
    with open(metric_file, "a") as f:
        for interval in intervals:
            interval = int(interval)
            # get optical flow and occlusion map
            fw_flow_dir = os.path.join(args.flow_dir, "fw_flow_%d"%interval)
            fw_occ_dir = os.path.join(args.flow_dir, "fw_occlusion_%d"%interval)
            flow_files = sorted(glob.glob(os.path.join(fw_flow_dir, '*.flo')), key=sort_key)
            occ_files = sorted(glob.glob(os.path.join(fw_occ_dir, '*.png')), key=sort_key)
            # assert len(flow_files) == len(occ_files)
            # assert len(flow_files) == (len(frames)-interval)

            err = 0 # MSE
            dist = 0 # LPIPS
            cnt = 0 # evaluated frames
            for f_id in tqdm(range(0, len(frames)-interval)):

                ### load input images
                imfile1 = frames[f_id]
                imfile2 = frames[f_id + interval]
                
                image1 = load_image(imfile1, args.max_side, device) #[1,3,H,W]
                image2 = load_image(imfile2, args.max_side, device)

                ### load flow
                flow = torch.from_numpy(frame_utils.readFlow(flow_files[cnt])).permute(2, 0, 1)[None, ...].to(device) #[1,2,H,W]

                ### load occlusion mask
                occ_mask = load_image(occ_files[cnt], args.max_side, device, mode="L")[0] #[H,W]
                noc_mask = 1 - occ_mask            
                N = torch.sum(noc_mask)

                ## warp img2
                warpped_img21 = warp(image2, flow) # warp image2 back to image1

                if N > 0:
                    ## compute warping MSE
                    diff = (warpped_img21 - image1) * noc_mask #[1,3,H,W]
                    diff = diff[0]
                    err += torch.sum(torch.square(diff)) / N

                    ## compute warping LPIPS
                    with torch.no_grad():
                        masked_warp_img21 = warpped_img21 * noc_mask
                        masked_gt_img1 = image1 * noc_mask
                        # dist += loss_fn_alex(masked_warp_img21, masked_gt_img1).view(-1)[0]

                        dist_layers = loss_fn_alex(masked_warp_img21, masked_gt_img1, retPerLayer=False, normalize=True) # input value in [0,1] need normalizing to [-1,1]
                        # print("dist_layers.shape", dist_layers.shape) #[1,1,H,W]
                        dist_layers = dist_layers[0,0,...]
                        dist += torch.sum(dist_layers * noc_mask) / N

                cnt += 1
                if cnt % 10 == 0:
                    print("First#%d, MSE: %.4f, Mean LPIPS: %.4f"%(cnt, err/cnt, dist/cnt))
                # f.write("First#%d, MSE: %.4f, LPIPS: %.4f\n"%(cnt, err/cnt, dist/cnt))

                
            err_all = err / cnt
            dist_all = dist / cnt
            print("Average Warping MSE = %f" %(err_all))
            print("Average Warping LPIPS = %f" %(dist_all))
            f.write("range: %d, Mean Warp MSE: %f\n"%(interval,err_all))
            f.write("range: %d, Mean Warp LPIPS: %f\n"%(interval, dist_all))
