import sys
sys.path.append('core')

import argparse
import os
import cv2
import glob
import numpy as np
import torch
from PIL import Image

from raft import RAFT
from utils import flow_viz
from utils.utils import InputPadder
from tqdm import tqdm
from utils.utils import InputPadder, coords_grid, bilinear_sampler, warp



DEVICE = 'cuda'

def load_image(imfile):
    img = np.array(Image.open(imfile).convert("RGB")).astype(np.uint8)
    img = torch.from_numpy(img).permute(2, 0, 1).float()
    return img[None].to(DEVICE)


def save_viz_flow(img, flo, imfile, output_path):
    img = img[0].permute(1,2,0).cpu().numpy()
    flo = flo[0].permute(1,2,0).cpu().numpy()
    
    # map flow to rgb image
    flo = flow_viz.flow_to_image(flo)
    img_flo = np.concatenate([img, flo], axis=0)
    # print(img_flo.shape) #HxWxC
    flow_img = Image.fromarray(flo.astype(np.uint8))
    filename = os.path.join(output_path, os.path.basename(imfile))
    flow_img.save(filename)
 
def sort_key(x):
    x = os.path.basename(x)
    if len(x) > 2 and x[0]=='r' and x[1] == '_': #syn
        return int(x[2:].split(".")[0])
    elif len(x) > 2 and x[1] == '_': #nsvf
        return x[2:]
    else:
        return x

def demo(args):
    model = torch.nn.DataParallel(RAFT(args))
    model.load_state_dict(torch.load(args.model))

    model = model.module
    model.to(DEVICE)
    model.eval()
    thresh=1.0

    all_flow = []

    with torch.no_grad():
        images = glob.glob(os.path.join(args.path, '*.png')) + \
                 glob.glob(os.path.join(args.path, '*.jpg')) + \
                 glob.glob(os.path.join(args.path, '*.JPG'))
        
        images = sorted(images, key=sort_key)
        for imfile1, imfile2 in zip(images[:-1], tqdm(images[1:])):
            image1 = load_image(imfile1)
            image2 = load_image(imfile2)

            padder = InputPadder(image1.shape)
            image1, image2 = padder.pad(image1, image2)

            flow_low, flow_up = model(image1, image2, iters=20, test_mode=True)
            save_viz_flow(image1, flow_up, imfile1, args.output_path)
            # all_flow.append(flow_up.cpu().numpy())


            # occlussion map
            _, flow12 = model(image1, image2, iters=24, test_mode=True)
            _, flow21 = model(image2, image1, iters=24, test_mode=True)

            coords0 = coords_grid(1, image1.shape[2], image1.shape[3]).cuda()
            coords1 = coords0 + flow12
            coords2 = coords1 + bilinear_sampler(flow21, coords1.permute(0,2,3,1))

            err = (coords0 - coords2).norm(dim=1)
            occ = (err[0] > thresh).float().cuda() 
            nocc = 1. - occ #==> non-occlusion map for image1
            # print("occ.shape", occ.shape) #H,W
            
            occ_img = Image.fromarray((occ.cpu().numpy() * 255.).astype(np.uint8))
            filename = os.path.join(args.output_path, "occ_"+os.path.basename(imfile1))
            occ_img.save(filename)



            # warpped image
            warpped_img21 = warp(image2, flow12) # warp image2 back to image1
            # warpped_img21 = warp(image2, flow21)
            masked_warpped_img1 = warpped_img21 * nocc
            masked_img1_gt = image1 * nocc
            # print("warpped_img1.shape", warpped_img1.shape) # [1,3,H,W]

            # masked warpped image
            warpped_img1 = warpped_img21
            warpped_img1 = warpped_img1[0].permute(1,2,0).cpu().numpy()
            warpped_img1 = Image.fromarray(warpped_img1.astype(np.uint8))
            filename = os.path.join(args.output_path, "warpback_"+os.path.basename(imfile1))
            warpped_img1.save(filename)

            masked_warpped_img1 = masked_warpped_img1[0].permute(1,2,0).cpu().numpy()
            masked_warpped_img1 = Image.fromarray(masked_warpped_img1.astype(np.uint8))
            filename = os.path.join(args.output_path, "warpback_mask_"+os.path.basename(imfile1))
            masked_warpped_img1.save(filename)

            masked_img1_gt = masked_img1_gt[0].permute(1,2,0).cpu().numpy()
            masked_img1_gt = Image.fromarray(masked_img1_gt.astype(np.uint8))
            filename = os.path.join(args.output_path, "warpback_mask_gt_"+os.path.basename(imfile1))
            masked_img1_gt.save(filename)


        # all_flow = np.array(all_flow) #B-1, C, H, W
        # npname = os.path.join(args.output_path, "flows.npy")
        # np.save(npname, all_flow)




'''
python demo_save.py \
--model models/raft-sintel.pth \
--path ../svox2/dataset/nerf_synthetic/chair/test_path \
--output_path demo-results \
--mixed_precision

python demo_save.py \
--model models/raft-things.pth \
--path ../svox2/dataset/nerf_synthetic/chair/test_path \
--output_path demo-results \
--mixed_precision
'''

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--model', help="restore checkpoint")
    parser.add_argument('--path', help="dataset for evaluation")
    parser.add_argument('--output_path', help="output flows")
    parser.add_argument('--small', action='store_true', help='use small model')
    parser.add_argument('--mixed_precision', action='store_true', help='use mixed precision')
    parser.add_argument('--alternate_corr', action='store_true', help='use efficent correlation implementation')
    args = parser.parse_args()

    demo(args)
