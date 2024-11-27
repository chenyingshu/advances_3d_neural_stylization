'''
Source code for
Advances in 3D Neural Stylization: A Survey
Script for evaluating ClipScore and ClipVar.
'''

import os
import json
import numpy as np
import torch
from PIL import Image
from transformers import CLIPProcessor, CLIPModel
from sklearn.metrics.pairwise import cosine_similarity
from tqdm import tqdm
import torch.nn.functional as F

# Initialize CLIP model and processor
device = "cuda:0" if torch.cuda.is_available() else "cpu"
model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32").to(device)
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")


def calculate_clip_score(image, text):
    """Calculate CLIP score for a given image and text."""
    image = Image.open(image).convert("RGB")
    inputs = processor(text=[text], images=image, return_tensors="pt", padding=True).to(device)
    outputs = model(**inputs)
    logits_per_image = outputs.logits_per_image
    return logits_per_image.item()


def calculate_clip_score_images(image_path1, image_path2):
    """Calculate CLIP score for 2 given images."""
    # Load the images
    image1 = Image.open(image_path1)
    image2 = Image.open(image_path2)

    # Preprocess the images for the CLIP model
    inputs = processor(images=[image1, image2], return_tensors="pt", padding=True).to(device)

    # Get the image features from the CLIP model
    with torch.no_grad():
        image_features = model.get_image_features(**inputs)

    # Normalize the image features
    image_features = image_features / image_features.norm(p=2, dim=-1, keepdim=True)

    # Compute cosine similarity between the two image features
    cosine_similarity = torch.matmul(image_features[0], image_features[1].T)

    # Convert the cosine similarity to a scalar value (float)
    clip_score = cosine_similarity.item()

    return clip_score


def calculate_clip_variance(image_paths):
    """
    Calculate the CLIP variance metric by computing the minimum cosine similarity
    between features extracted from multi-view rendering images using CLIP.

    Parameters:
    - image_paths: List of file paths to the images for which the metric is calculated.

    Returns:
    - min_cosine_similarity: The minimum cosine similarity between image feature vectors.
    """
    # Load and preprocess images
    images = [Image.open(image_path) for image_path in image_paths]

    # Preprocess images and extract features using CLIP
    inputs = processor(images=images, return_tensors="pt", padding=True).to(device)
    outputs = model.get_image_features(**inputs)

    # Normalize the image features
    image_features = outputs / outputs.norm(p=2, dim=-1, keepdim=True)  # Normalize to unit vectors

    # Calculate cosine similarities between each pair of features
    cos_sim_matrix = cosine_similarity(image_features.cpu().detach().numpy())

    # Set diagonal values to -1 to avoid considering self-similarity
    np.fill_diagonal(cos_sim_matrix, 1)

    # Get the minimum cosine similarity from the off-diagonal elements
    min_cosine_similarity = cos_sim_matrix.min()

    return min_cosine_similarity.item()


# Path to the parent directory containing sub-directories
base_dir = '/path/to/your/rendering'

# Dictionary to store the clipscore for each sub-directory
clipscore_results = {}
clipvar_results = {}

# List of image filenames
image_files = ['000_rgb.png', '001_rgb.png', '002_rgb.png', '003_rgb.png']  # specify the rendered images under each directory

# Iterate over all sub-directories in the base directory
for subdir in tqdm(os.listdir(base_dir)):
    subdir_path = os.path.join(base_dir, subdir)
    subdir_name = subdir.split('-')[0]
    # if calculate clip-score between 2 images
    # style_image = os.path.join('/path/to/your/style/reference/directory', subdir_name, '000.png')
    style_prompt = 'your_prompt'
    if os.path.isdir(subdir_path):  # Only process directories
        clipscores = []
        image_paths = []

        # Check and calculate clipscore for each image file
        for image_file in image_files:
            image_path = os.path.join(subdir_path, image_file)
            if os.path.exists(image_path):
                clipscore = calculate_clip_score(image_path, style_prompt)
                # clipscore = calculate_clip_score_images(image_path, style_image)
                clipscores.append(clipscore)
            image_paths.append(image_path)
        clipvar = calculate_clip_variance(image_paths)
        clipvar_results[subdir_name] = clipvar

        if clipscores:
            # Calculate the average clipscore for the current sub-directory
            avg_clipscore = np.mean(clipscores)
            clipscore_results[subdir_name] = avg_clipscore

# Calculate the overall average clipscore
overall_clipscore = np.mean(list(clipscore_results.values())) if clipscore_results else 0
overall_clipvar = np.mean(list(clipvar_results.values())) if clipvar_results else 0

# Add the overall average clipscore to the results
clipscore_results['overall'] = overall_clipscore
clipvar_results['overall'] = overall_clipvar

# Write the results to a JSON file
output_file1 = 'clip-score.json'
with open(output_file1, 'w') as f:
    json.dump(clipscore_results, f, indent=4)

print(f"Results written to {output_file1}")

output_file2 = 'clip-var.json'
with open(output_file2, 'w') as f:
    json.dump(clipvar_results, f, indent=4)

print(f"Results written to {output_file2}")
