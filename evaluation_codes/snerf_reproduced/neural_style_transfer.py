'''
Source code for
Advances in 3D Neural Stylization: A Survey

Adapted from https://pytorch.org/tutorials/advanced/neural_style_tutorial.html 
based on implementation on SNeRF original paper
It is for SNeRF stylization
'''


import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

from PIL import Image
import numpy as np

import torchvision.transforms as transforms
import torchvision.models as models

import argparse
import os 
import glob
from tqdm import tqdm


class ContentLoss(nn.Module):

    def __init__(self, target,):
        super(ContentLoss, self).__init__()
        self.target = target.detach()

    def forward(self, input):
        self.loss = F.mse_loss(input, self.target)
        return input

def gram_matrix(input):
    a, b, c, d = input.size()  # a=batch size(=1)

    features = input.view(a * b, c * d)  # resize F_XL into \hat F_XL

    G = torch.mm(features, features.t())  # compute the gram product
    return G.div(a * b * c * d)


class StyleLoss(nn.Module):

    def __init__(self, target_feature):
        super(StyleLoss, self).__init__()
        self.target = gram_matrix(target_feature).detach()

    def forward(self, input):
        G = gram_matrix(input)
        self.loss = F.mse_loss(G, self.target)
        return input


######################################################################
# Importing the Model
# -------------------
cnn = models.vgg16(pretrained=True).features.eval()

cnn_normalization_mean = [0.485, 0.456, 0.406]
cnn_normalization_std = [0.229, 0.224, 0.225]


class Normalization(nn.Module):
    def __init__(self, mean, std, device):
        super(Normalization, self).__init__()
        self.mean = torch.tensor(mean).view(-1, 1, 1).to(device)
        self.std = torch.tensor(std).view(-1, 1, 1).to(device)

    def forward(self, img):
        # normalize ``img``
        return (img - self.mean) / self.std

content_layers_default = ['relu_8'] # Relu4_1
style_layers_default = ['relu_1', 'relu_3', 'relu_5', 'relu_8'] # Relu1~4_1

def get_style_model_and_losses(cnn, normalization_mean, normalization_std,
                               style_img, content_img, device,
                               content_layers=content_layers_default,
                               style_layers=style_layers_default):
    # normalization module
    normalization = Normalization(normalization_mean, normalization_std, device)

    # just in order to have an iterable access to or list of content/style
    # losses
    content_losses = []
    style_losses = []

    model = nn.Sequential(normalization).to(device)

    i = 0  # increment every time we see a conv
    for layer in cnn.children():
        if isinstance(layer, nn.Conv2d):
            i += 1
            name = 'conv_{}'.format(i)
        elif isinstance(layer, nn.ReLU):
            name = 'relu_{}'.format(i)
            layer = nn.ReLU(inplace=False)
        elif isinstance(layer, nn.MaxPool2d):
            name = 'pool_{}'.format(i)
        elif isinstance(layer, nn.BatchNorm2d):
            name = 'bn_{}'.format(i)
        else:
            raise RuntimeError('Unrecognized layer: {}'.format(layer.__class__.__name__))

        model.add_module(name, layer.to(device))

        if name in content_layers:
            # add content loss:
            target = model(content_img).detach()
            content_loss = ContentLoss(target)
            model.add_module("content_loss_{}".format(i), content_loss)
            content_losses.append(content_loss)

        if name in style_layers:
            # add style loss:
            target_feature = model(style_img).detach()
            style_loss = StyleLoss(target_feature)
            model.add_module("style_loss_{}".format(i), style_loss)
            style_losses.append(style_loss)

    # now we trim off the layers after the last content and style losses
    for i in range(len(model) - 1, -1, -1):
        if isinstance(model[i], ContentLoss) or isinstance(model[i], StyleLoss):
            break

    model = model[:(i + 1)]

    return model, style_losses, content_losses


def get_input_optimizer(input_img):
    # this line to show that input is a parameter that requires a gradient
    optimizer = optim.LBFGS([input_img])
    return optimizer


def run_style_transfer(cnn, normalization_mean, normalization_std,
                       content_img, style_img, input_img, device, num_steps=500,
                       style_weight=1000000, content_weight=1):
    """Run the style transfer."""
    print('Building the style transfer model..')
    model, style_losses, content_losses = get_style_model_and_losses(cnn,
        normalization_mean, normalization_std, style_img, content_img, device=device)

    input_img.requires_grad_(True)
    model.eval()
    model.requires_grad_(False)

    optimizer = get_input_optimizer(input_img)

    print('Optimizing..')
    run = [0]
    while run[0] <= num_steps:

        def closure():
            # correct the values of updated input image
            with torch.no_grad():
                input_img.clamp_(0, 1)

            optimizer.zero_grad()
            model(input_img)
            style_score = 0
            content_score = 0

            for sl in style_losses:
                style_score += sl.loss
            for cl in content_losses:
                content_score += cl.loss

            style_score *= style_weight
            content_score *= content_weight

            loss = style_score + content_score
            loss.backward()

            run[0] += 1
            return style_score + content_score

        optimizer.step(closure)

    # a last correction...
    with torch.no_grad():
        input_img.clamp_(0, 1)

    return input_img

def image_loader(image_name, imsize, device):
    loader = transforms.Compose([
        transforms.Resize((imsize,imsize)),  # scale imported image
        transforms.ToTensor()])  # transform it into a torch tensor
    image = Image.open(image_name).convert("RGB")
    # fake batch dimension required to fit network's input dimensions
    image = loader(image).unsqueeze(0)
    return image.to(device)


def sort_key(x):
    x = os.path.basename(x)
    if len(x) > 2 and x[0]=='r' and x[1] == '_': #syn
        return int(x[2:].split(".")[0])
    elif len(x) > 2 and x[1] == '_': #nsvf
        return x[2:]
    else:
        return x


parser = argparse.ArgumentParser()
parser.add_argument('--content_dir', '-c', type=str, help='content image directory')
parser.add_argument('--style', '-s', type=str, help='style image')
parser.add_argument('--output_dir', '-o', type=str, help='output image path')
parser.add_argument('--extra_output_dirs', type=str, help='output image path') #"images_4,image_8"
parser.add_argument('--iter', type=int, default=500, help='optimization iterations')
parser.add_argument('--imsize', type=int, default="512", help='image size')
parser.add_argument('--weight_content', type=int, default=1, help='content weight')
parser.add_argument('--weight_style', type=float, default=1000000, help='style weight')
args = parser.parse_args()

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
# torch.set_default_device(device)

######################################################################
# Loading the Images

# desired size of the output image
imsize = args.imsize
style_img = image_loader(args.style, imsize, device)
content_paths = sorted(glob.glob(os.path.join(args.content_dir, "*")), key=sort_key)

extra_content_paths = []
extra_output_dirs = []
if args.extra_output_dirs is not None:
    extra_output_dirs = args.extra_output_dirs.split(",")
    for edir in extra_output_dirs:
        extra_content_paths.append(sorted(glob.glob(os.path.join(os.path.dirname(args.output_dir), edir, "*")), key=sort_key))

output_paths = sorted(glob.glob(os.path.join(args.output_dir, "*")), key=sort_key)


print("Stylizing %d images with style %s"%(len(content_paths), os.path.basename(args.style)))
for cid, content_path in enumerate(tqdm(content_paths)):

    content_img = image_loader(content_path, imsize, device)

    ######################################################################
    # Next, we select the input image. You can use a copy of the content image or white noise.
    input_img = content_img.clone() # SNerf is sensitive on content inconsistency
    # if you want to use white noise by using the following code:
    # input_img = torch.randn(content_img.data.size())

    # stylization
    output = run_style_transfer(cnn, cnn_normalization_mean, cnn_normalization_std,
                                content_img, style_img, input_img,
                                device=device, num_steps=args.iter,
                                style_weight=args.weight_style, content_weight=args.weight_content)

    ######################################################################
    # Save output image
    if not os.path.exists(os.path.dirname(args.output_dir)):
        os.makedirs(os.path.dirname(args.output_dir))
    output = (output[0].detach().cpu().numpy() * 255.).transpose(1,2,0).astype(np.uint8)
    output = Image.fromarray(output)

    tgt_img = Image.open(content_path)
    im = output.resize(tgt_img.size) #w,h original size
    im_filename = os.path.join(args.output_dir, os.path.basename(output_paths[cid]))
    im.save(im_filename)

    if args.extra_output_dirs is not None:
        for eid in range(len(extra_content_paths)):
            epath = extra_content_paths[eid][cid]
            tgt_img = Image.open(epath)
            im = output.resize(tgt_img.size) #w,h original size            
            im_filename = os.path.join(os.path.dirname(args.output_dir), extra_output_dirs[eid], os.path.basename(epath))  
            im.save(im_filename)
        



