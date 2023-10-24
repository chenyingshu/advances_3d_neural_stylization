''' by Yingshu Chen
ref: https://pytorch.org/hub/pytorch_vision_vgg/
VGG(
  (features): Sequential(
    (0): Conv2d(3, 64, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
    (1): ReLU(inplace=True) #Relu1_1
    (2): Conv2d(64, 64, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
    (3): ReLU(inplace=True) ##Relu1_2
    (4): MaxPool2d(kernel_size=2, stride=2, padding=0, dilation=1, ceil_mode=False)
    (5): Conv2d(64, 128, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
    (6): ReLU(inplace=True) #Relu2_1
    (7): Conv2d(128, 128, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
    (8): ReLU(inplace=True) #Relu2_2
    (9): MaxPool2d(kernel_size=2, stride=2, padding=0, dilation=1, ceil_mode=False)
    (10): Conv2d(128, 256, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
    (11): ReLU(inplace=True) #Relu3_1
    (12): Conv2d(256, 256, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
    (13): ReLU(inplace=True) #Relu3_2
    (14): Conv2d(256, 256, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
    (15): ReLU(inplace=True) #Relu3_3
    (16): Conv2d(256, 256, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
    (17): ReLU(inplace=True) #Relu3_4
    (18): MaxPool2d(kernel_size=2, stride=2, padding=0, dilation=1, ceil_mode=False)
    (19): Conv2d(256, 512, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
    (20): ReLU(inplace=True) #Relu4_1
    (21): Conv2d(512, 512, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
    (22): ReLU(inplace=True) #Relu4_2
    (23): Conv2d(512, 512, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
    (24): ReLU(inplace=True) #Relu4_3
    (25): Conv2d(512, 512, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
    (26): ReLU(inplace=True) #Relu4_4
    (27): MaxPool2d(kernel_size=2, stride=2, padding=0, dilation=1, ceil_mode=False)
    (28): Conv2d(512, 512, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
    (29): ReLU(inplace=True) #Relu5_1
    (30): Conv2d(512, 512, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
    (31): ReLU(inplace=True)
    (32): Conv2d(512, 512, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
    (33): ReLU(inplace=True) 
    (34): Conv2d(512, 512, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
    (35): ReLU(inplace=True) 
    (36): MaxPool2d(kernel_size=2, stride=2, padding=0, dilation=1, ceil_mode=False)
  )
  (avgpool): AdaptiveAvgPool2d(output_size=(7, 7))
  (classifier): Sequential(
    (0): Linear(in_features=25088, out_features=4096, bias=True)
    (1): ReLU(inplace=True)
    (2): Dropout(p=0.5, inplace=False)
    (3): Linear(in_features=4096, out_features=4096, bias=True)
    (4): ReLU(inplace=True)
    (5): Dropout(p=0.5, inplace=False)
    (6): Linear(in_features=4096, out_features=1000, bias=True)
  )
)
'''

from collections import namedtuple

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
        if len(gpu_ids) > 1:
            enc_1 = nn.DataParallel(nn.Sequential(*enc_layers[:2]).to(gpu_ids[0]), gpu_ids)  # [        -> relu1-1] C->64
            enc_2 = nn.DataParallel(nn.Sequential(*enc_layers[2:7]).to(gpu_ids[0]), gpu_ids)  # (relu1-1 -> relu2-1] 64->128
            enc_3 = nn.DataParallel(nn.Sequential(*enc_layers[7:12]).to(gpu_ids[0]), gpu_ids) # (relu2-1 -> relu3-1] 128->256
            enc_4 = nn.DataParallel(nn.Sequential(*enc_layers[12:21]).to(gpu_ids[0]), gpu_ids) # (relu3-1 -> relu4-1] 256->512
            enc_5 = nn.DataParallel(nn.Sequential(*enc_layers[21:30]).to(gpu_ids[0]), gpu_ids) # (relu4-1 -> relu5-1] 512->512
        else:
            enc_1 = nn.Sequential(*enc_layers[:2]).to(device)  # [        -> relu1-1] C->64
            enc_2 = nn.Sequential(*enc_layers[2:7]).to(device)  # (relu1-1 -> relu2-1] 64->128
            enc_3 = nn.Sequential(*enc_layers[7:12]).to(device) # (relu2-1 -> relu3-1] 128->256
            enc_4 = nn.Sequential(*enc_layers[12:21]).to(device) # (relu3-1 -> relu4-1] 256->512
            enc_5 = nn.Sequential(*enc_layers[21:30]).to(device) # (relu4-1 -> relu5-1] 512->512

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
