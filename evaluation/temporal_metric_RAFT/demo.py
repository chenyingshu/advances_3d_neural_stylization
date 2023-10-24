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
from utils.utils import InputPadder, coords_grid, bilinear_sampler



DEVICE = 'cuda'

def load_image(imfile):
    img = np.array(Image.open(imfile)).astype(np.uint8)
    img = torch.from_numpy(img).permute(2, 0, 1).float()
    return img[None].to(DEVICE)


def viz(img, flo):
    img = img[0].permute(1,2,0).cpu().numpy()
    flo = flo[0].permute(1,2,0).cpu().numpy()
    
    # map flow to rgb image
    flo = flow_viz.flow_to_image(flo)
    img_flo = np.concatenate([img, flo], axis=0)

    # import matplotlib.pyplot as plt
    # plt.imshow(img_flo / 255.0)
    # plt.show()

    cv2.imshow('image', img_flo[:, :, [2,1,0]]/255.0)
    cv2.waitKey()


def demo(args):
    # model = torch.nn.DataParallel(RAFT(args))
    # model.load_state_dict(torch.load(args.model))

    # model = model.module
    # model.to(DEVICE)
    # model.eval()

    # with torch.no_grad():
    #     images = glob.glob(os.path.join(args.path, '*.png')) + \
    #              glob.glob(os.path.join(args.path, '*.jpg'))
        
    #     images = sorted(images)
    #     for imfile1, imfile2 in zip(images[:-1], images[1:]):
    #         image1 = load_image(imfile1)
    #         image2 = load_image(imfile2)

    #         padder = InputPadder(image1.shape)
    #         image1, image2 = padder.pad(image1, image2)

    #         flow_low, flow_up = model(image1, image2, iters=20, test_mode=True)
    #         viz(image1, flow_up)


    # occlusion demo: https://github.com/princeton-vl/RAFT/issues/57
    thresh=1.0
    model = torch.nn.DataParallel(RAFT(args))
    model.load_state_dict(torch.load(args.model))

    model = model.module
    model.to(DEVICE)
    model.eval()

    with torch.no_grad():
        images = glob.glob(os.path.join(args.path, '*.png')) + \
                 glob.glob(os.path.join(args.path, '*.jpg'))
        
        images = sorted(images)
        for imfile1, imfile2 in zip(images[:-1], images[1:]):
            image1 = load_image(imfile1)
            image2 = load_image(imfile2)

            padder = InputPadder(image1.shape)
            image1, image2 = padder.pad(image1, image2)

            _, flow12 = model(image1, image2, iters=24, test_mode=True)
            _, flow21 = model(image2, image1, iters=24, test_mode=True)

            coords0 = coords_grid(1, image1.shape[2], image1.shape[3]).cuda()
            coords1 = coords0 + flow12
            coords2 = coords1 + bilinear_sampler(flow21, coords1.permute(0,2,3,1))

            err = (coords0 - coords2).norm(dim=1)
            occ = (err[0] > thresh).float().cpu().numpy()
            print("occ.shape", occ.shape)

            # cv2.imshow('occ', occ)
            # cv2.waitKey()
'''
python demo.py \
--model models/raft-sintel.pth \
--path ../svox2/dataset/nerf_llff_data/fern/images_4 \
--mixed_precision
'''
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--model', help="restore checkpoint")
    parser.add_argument('--path', help="dataset for evaluation")
    parser.add_argument('--small', action='store_true', help='use small model')
    parser.add_argument('--mixed_precision', action='store_true', help='use mixed precision')
    parser.add_argument('--alternate_corr', action='store_true', help='use efficent correlation implementation')
    args = parser.parse_args()

    demo(args)
