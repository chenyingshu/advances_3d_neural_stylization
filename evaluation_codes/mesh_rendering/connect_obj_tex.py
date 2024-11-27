'''
Source code for
Advances in 3D Neural Stylization: A Survey
Script for connecting texture image with mesh object (for methods like TexPainter).
'''

import os
import shutil

# Define the root directories
tex_painter_root = '/path/to/TexPainter/Results/'
objaverse_root = '/path/to/objaverse/'

# Get all directories in the TexPainter results folder
directories = [d for d in os.listdir(tex_painter_root) if os.path.isdir(os.path.join(tex_painter_root, d))]

for directory in directories:
    tex_result_path = os.path.join(tex_painter_root, directory, 'tex_result.png')
    obj_dir_path = os.path.join(objaverse_root, directory)
    obj_path = os.path.join(obj_dir_path, 'mesh.obj')

    # Check if tex_result.png exists
    if os.path.exists(tex_result_path):
        # Ensure the target directory exists
        if not os.path.exists(obj_dir_path):
            os.makedirs(obj_dir_path)

        # Copy the tex_result.png to the new location
        shutil.copy(tex_result_path, os.path.join(obj_dir_path, 'mesh.png'))

        # Check if the .obj file exists
        if os.path.exists(obj_path):
            # Read the existing content of the .obj file
            with open(obj_path, 'r') as obj_file:
                obj_content = obj_file.readlines()

            # Add the required lines at the beginning
            obj_content.insert(0, 'mtllib mesh.mtl\n')
            obj_content.insert(1, 'usemtl mesh\n')

            # Write the modified content back to the .obj file
            with open(obj_path, 'w') as obj_file:
                obj_file.writelines(obj_content)

        else:
            print(f"Warning: {obj_path} not found.")
    else:
        print(f"Warning: {tex_result_path} not found.")

print("Operation completed.")
