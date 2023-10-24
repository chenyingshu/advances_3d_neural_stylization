'''
by Yingshu Chen
ref: https://pytorch.org/tutorials/advanced/neural_style_tutorial.html#style-loss
'''

import argparse
import os
import sys
import time

import numpy as np
import torch
from torchvision import transforms
from torch.utils.data import DataLoader
import glob
from tqdm import tqdm

import utils
from utils import ImageFolder
from vgg import VGG19



def check_paths(args):
    assert os.path.exists(args.input_dir)
    assert not os.path.exists(args.output_file)


def compute_style_loss(args):
    # basic loading, setting
    device = torch.device("cuda" if len(args.gpu_ids) else "cpu")
    mse_loss = torch.nn.MSELoss()
    vgg = VGG19(device=device, requires_grad=False, gpu_ids=args.gpu_ids).to(device)
    
    # load generated image and target style image
    image_transform = transforms.Compose([
        transforms.Resize((args.image_size, args.image_size)),
        transforms.ToTensor()
    ])
    image_dateset = ImageFolder(args.input_dir, image_transform)
    image_dataloader = DataLoader(image_dateset, batch_size=args.batch_size, shuffle=False)
    style_image = image_transform(utils.default_loader(args.style_image))
    style_image = style_image.unsqueeze(0).to(device)

    with open(args.output_file, 'a') as f:
        sum_val = 0.0
        count = 0

        # for views
        for bid, batch_image in enumerate(tqdm(image_dataloader)):
            batch_image = batch_image.to(device).detach()

            # get VGG features
            features_input = vgg(batch_image)
            features_style = vgg(style_image.repeat(batch_image.shape[0],1,1,1))

            # calculate mse of gram matrices
            style_loss = 0.
            data = []
            for ft_y, ft_s in zip(features_input, features_style):
                gm_y = utils.gram_matrix(ft_y)
                gm_s = utils.gram_matrix(ft_s)
                style_loss += mse_loss(gm_y, gm_s)

            style_loss = style_loss * args.style_weight / len(features_input) 
            data.append(style_loss.data)
            f.write('batch %d: %.7f\n' %(bid, style_loss))

            style_loss_mean = sum(data) / len(data)
            count += 1
            sum_val += style_loss_mean

        m_style_loss = sum_val/count
        f.write('total_mean: %.7f\n'%m_style_loss)    
        print("Total Mean Style Loss: %.4f"%(m_style_loss))  



def main():
    '''
        python eval_style_loss.py \
        -i sample_data/image_dir/fern_snerf_iter1_14 \
        -style sample_data/style_dir/14.jpg \
        -o logs/fern_snerf_iter1_14.txt \
        --batch_size 8 \
        --image_size 256 \
        --gpu_ids 0,1,2,3
        

    '''
    parser = argparse.ArgumentParser(description="parser for neural-style-loss")
    parser.add_argument("--batch_size", type=int, default=1,
                                  help="batch size, default is 1")    
    parser.add_argument("--image_size", type=int, default=256,
                                  help="size of images, default is 256 X 256")
    parser.add_argument("--style_weight", type=float, help="weight factor for style loss, default=3e4, in range of [0,10], default=1e10", default=1e5)
    parser.add_argument("--input_dir", '-i', type=str,
                                 help="path of generated images to compute style loss")
    parser.add_argument("--style_image", '-style', type=str,
                                 help="path of target style image to compute style loss")
    parser.add_argument("--output_file", '-o', type=str, default='logs/fern_snerf_14.txt',
                                 help="path of save style loss record")
    parser.add_argument('--gpu_ids', type=str, default='0', help='gpu ids: e.g. 0  0,1,2, 0,2. use -1 for CPU')

    args = parser.parse_args()
    str_ids = args.gpu_ids.split(',')
    gpu_ids = []
    for str_id in str_ids:
        id = int(str_id)
        if id >= 0:
            gpu_ids.append(id)
    args.gpu_ids = gpu_ids

    if (len(args.gpu_ids) > 0) and not torch.cuda.is_available():
        print("WARNING: cuda is not available, try running on CPU")
        args.gpu_ids = []

    tot_num = len(glob.glob(os.path.join(args.input_dir,"*")))
    if tot_num % args.batch_size != 0:
        print("Please use the divisor of the number of images as batch size.")
        print("Change batch size to 1.")
        args.batch_size = 1

    # check_paths(args)
    compute_style_loss(args)


if __name__ == "__main__":
    start_time = time.time()
    main()
    print('Time elapsed: %4.f sec' %((time.time()- start_time)))