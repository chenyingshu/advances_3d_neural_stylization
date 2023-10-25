'''
This work is licensed under CC BY-NC-SA 4.0 

Adapted from https://github.com/phoenix104104/fast_blind_video_consistency/blob/master/compute_flow_occlusion.py
By Yingshu Chen

This script is to:
1. estimate optical flow for testing sequence
2. compute occlusion masks for testing sequence

CUDA_VISIBLE_DEVICES=0 python compute_flow_occlusion.py \
--model models/raft-sintel.pth \
--mixed_precision \
--data_dir ../results/nerf_synthetic/chair/test_path \
--out_dir ../results/nerf_synthetic/chair/optical_flow 

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
from utils.utils import InputPadder, forward_interpolate, coords_grid, bilinear_sampler, warp
from tqdm import tqdm


def load_image(imfile, resize=1024, device='cuda'):
    img = Image.open(imfile).convert("RGB")
    w,h = img.size
    if (w >= h) and (w > resize):
        new_w = resize
        new_h = int(1.0 * new_w / w * h)
        img = img.resize((new_w, new_h))
    elif (h > w) and (h > resize):
        new_h = resize
        new_w = int(1.0 * new_h / h * w)
        img = img.resize((new_w, new_h))

    img = np.array(img).astype(np.uint8)
    img = torch.from_numpy(img).permute(2, 0, 1).float()
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

    parser = argparse.ArgumentParser(description='optical flow estimation')

    ### testing options
    parser.add_argument('--model',          type=str,               default="models/raft-sintel.pth",   help="RAFT model restore checkpoint")
    parser.add_argument('--iters',          type=int,               default=24,                         help='path to stylized data folder')
    parser.add_argument('--small',          action='store_true',    help='use small model')
    parser.add_argument('--mixed_precision',action='store_true',    help='use mixed precision')
    parser.add_argument('--alternate_corr', action='store_true',    help='use efficent correlation implementation')

    parser.add_argument('--data_dir', type=str,  default='data/scene/path',   help='path to data folder')
    parser.add_argument('--out_dir',  type=str,  default='results/scene',help='path to output folder')

    parser.add_argument('--intervals', default=[1,10], help='short/long range, 1 or 10')
    parser.add_argument('--max_side', type=int, default=1024, help='maximum image side')

    args = parser.parse_args()
    # print(args)

    if torch.cuda.is_available():
        device = torch.device("cuda") 
    else:
        raise Exception("Error: No GPU found.")
        exit;

    # load sequence frame paths
    exts = ['.png', '.jpg', '.jpeg', '.exr']
    frames = os.listdir(args.data_dir)
    frames =sorted([os.path.join(args.data_dir, x) for x in frames if not x.startswith('.') and any((x.lower().endswith(ext) for ext in exts))], key=sort_key)

    # load model
    print("===> Load %s" %args.model)
    model = torch.nn.DataParallel(RAFT(args))
    model.load_state_dict(torch.load(args.model))

    model = model.module
    model.to(device)
    model.eval()

    thresh = 1.

    # different ranges
    for interval in args.intervals:

        # create output directory
        fw_flow_dir = os.path.join(args.out_dir, "fw_flow_%d"%interval)
        if not os.path.isdir(fw_flow_dir):
            os.makedirs(fw_flow_dir)
        fw_occ_dir = os.path.join(args.out_dir, "fw_occlusion_%d"%interval)
        if not os.path.isdir(fw_occ_dir):
            os.makedirs(fw_occ_dir)

        with torch.no_grad():
            for f_id in tqdm(range(0, len(frames)-interval, interval)):
                imfile1 = frames[f_id]
                imfile2 = frames[f_id + interval]
                
                image1 = load_image(imfile1, args.max_side, device)
                image2 = load_image(imfile2, args.max_side, device)
                padder = InputPadder(image1.shape)
                image1, image2 = padder.pad(image1, image2) # make sure image divisible by 8

                # estimate optical flow
                _, flow12 = model(image1, image2, iters=args.iters, test_mode=True)
                flow = padder.unpad(flow12[0]).permute(1, 2, 0).cpu().numpy()
                output_file = os.path.join(fw_flow_dir, os.path.basename(imfile1).split('.')[0]+'.flo')
                frame_utils.writeFlow(output_file, flow)

                # compute occlussion map, adapted from https://github.com/princeton-vl/RAFT/issues/57
                _, flow21 = model(image2, image1, iters=args.iters, test_mode=True)
                coords0 = coords_grid(1, image1.shape[2], image1.shape[3]).cuda()
                coords1 = coords0 + flow12
                coords2 = coords1 + bilinear_sampler(flow21, coords1.permute(0,2,3,1))

                err = (coords0 - coords2).norm(dim=1)
                occ = (err[0] > thresh).float().cuda() 
                occ = padder.unpad(occ)
                # print("occ.shape", occ.shape) #H,W            
                occ_img = Image.fromarray((occ.cpu().numpy() * 255.).astype(np.uint8))
                filename = os.path.join(fw_occ_dir, os.path.basename(imfile1).split(".")[0]+".png")
                occ_img.save(filename)



