'''
Source code for
Advances in 3D Neural Stylization: A Survey
'''

import torch
from torch import nn
from torchvision import models


# create a module to normalize input image so we can easily put it in a
# ``nn.Sequential``
class Normalization(nn.Module):
    def __init__(self, device):
        super(Normalization, self).__init__()
        # .view the mean and std to make them [C x 1 x 1] so that they can
        # directly work with image Tensor of shape [B x C x H x W].
        # B is batch size. C is number of channels. H is height and W is width.
        self.mean = torch.tensor([0.485, 0.456, 0.406]).view(-1, 1, 1).detach().to(device)
        self.std = torch.tensor([0.229, 0.224, 0.225]).view(-1, 1, 1).detach().to(device)

    def forward(self, img):
        # normalize ``img``
        return (img - self.mean) / self.std

class VGG19(torch.nn.Module):
    def __init__(self, device, requires_grad=False, gpu_ids=[0]):
        super(VGG19, self).__init__()
        self.normalization = Normalization(device)

        vgg_pretrained_features = models.vgg19(pretrained=True).features
        enc_layers = list(vgg_pretrained_features.children())
        if len(gpu_ids) > 0:
            enc_1 = nn.DataParallel(nn.Sequential(*enc_layers[:2]).to(gpu_ids[0]), gpu_ids)  # [        -> relu1-1] C->64
            enc_2 = nn.DataParallel(nn.Sequential(*enc_layers[2:7]).to(gpu_ids[0]), gpu_ids)  # (relu1-1 -> relu2-1] 64->128
            enc_3 = nn.DataParallel(nn.Sequential(*enc_layers[7:12]).to(gpu_ids[0]), gpu_ids) # (relu2-1 -> relu3-1] 128->256
            enc_4 = nn.DataParallel(nn.Sequential(*enc_layers[12:21]).to(gpu_ids[0]), gpu_ids) # (relu3-1 -> relu4-1] 256->512
            enc_5 = nn.DataParallel(nn.Sequential(*enc_layers[21:30]).to(gpu_ids[0]), gpu_ids) # (relu4-1 -> relu5-1] 512->512
        else:
            enc_1 = nn.Sequential(*enc_layers[:2])  # [        -> relu1-1] C->64
            enc_2 = nn.Sequential(*enc_layers[2:7])  # (relu1-1 -> relu2-1] 64->128
            enc_3 = nn.Sequential(*enc_layers[7:12]) # (relu2-1 -> relu3-1] 128->256
            enc_4 = nn.Sequential(*enc_layers[12:21]) # (relu3-1 -> relu4-1] 256->512
            enc_5 = nn.Sequential(*enc_layers[21:30]) # (relu4-1 -> relu5-1] 512->512

        self.image_encoder_layers = [enc_1, enc_2, enc_3, enc_4, enc_5]

        if not requires_grad:
            for param in self.parameters():
                param.requires_grad = False
        
    def forward(self, x):
        results = [self.normalization(x)]
        for i in range(len(self.image_encoder_layers)):
            func = self.image_encoder_layers[i]
            results.append(func(results[-1]))
        
        out = results[1:]
        return out
