''' by Yingshu Chen
'''
import os
import torch
import torch.utils.data as data
from PIL import Image, ImageChops, ImageOps

IMG_EXTENSIONS = [
    '.jpg', '.JPG', '.jpeg', '.JPEG', '.tif',
    '.png', '.PNG', '.ppm', '.PPM', '.bmp', '.BMP',
]

def default_loader(path):
    '''
        Load image using RGB color space
    '''
    return Image.open(path).convert('RGB')  

# def mask_loader(path):
#     return Image.open(path)[..., -1].convert('L')  


def is_image_file(filename):
    return any(filename.endswith(extension) for extension in IMG_EXTENSIONS)


def make_dataset(dir):
    images = []
    assert os.path.isdir(dir), '%s is not a valid directory' % dir

    for root, _, fnames in sorted(os.walk(dir)):
        for fname in fnames:
            if is_image_file(fname):
                path = os.path.join(root, fname)
                images.append(path)

    return images


class ImageFolder(data.Dataset):

    def __init__(self, root, transform=None, loader=default_loader):
        imgs = sorted(make_dataset(root))
        if len(imgs) == 0:
            raise(RuntimeError("Found 0 images in: " + root + "\n"
                               "Supported image extensions are: " +
                               ",".join(IMG_EXTENSIONS)))

        self.root = root
        self.imgs = sorted(imgs)
        self.transform = transform
        self.loader = loader

    def __getitem__(self, index):
        path = self.imgs[index]
        img = self.loader(path)
        # if self.new_size:
        #     width, height = img.size
        #     if width > height:
        #         new_width = int(width * (self.new_size/height) / 8 + 0.5) * 8
        #         img = img.resize((new_width, self.new_size))
        #     else:
        #         new_height = int(height * (self.new_size/width) / 8 + 0.5) * 8 
        #         img = img.resize((self.new_size, new_height))

        if self.transform is not None:
            img = self.transform(img)
        return img

    def __len__(self):
        return len(self.imgs)

def invert_image(im):
    return ImageOps.invert(im)

def apply_mask(mask, im2):
    return ImageChops.multiply(mask, im2)

# def load_image(filename, size=None, scale=None):
#     img = Image.open(filename).convert('RGB')
#     if size is not None:
#         img = img.resize((size, size), Image.ANTIALIAS)
#     elif scale is not None:
#         img = img.resize((int(img.size[0] / scale), int(img.size[1] / scale)), Image.ANTIALIAS)
#     return img


def save_image(filename, data):
    img = data.clone().clamp(0, 255).numpy()
    img = img.transpose(1, 2, 0).astype("uint8")
    img = Image.fromarray(img)
    img.save(filename)


def gram_matrix(y):
    (b, c, h, w) = y.size()
    features = y.view(b, c, w * h)
    features_t = features.transpose(1, 2)
    gram = features.bmm(features_t) / (c * h * w)
    return gram


def normalize_batch(batch):
    # normalize using imagenet mean and std
    mean = batch.new_tensor([0.485, 0.456, 0.406]).view(-1, 1, 1)
    std = batch.new_tensor([0.229, 0.224, 0.225]).view(-1, 1, 1)
    batch = batch.div_(255.0)
    return (batch - mean) / std
