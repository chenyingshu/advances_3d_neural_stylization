'''
Source code for
Advances in 3D Neural Stylization: A Survey
Script for rendering a list of textured objects.
'''

import os
import subprocess

# Root directory containing the subdirectories
root_dir = "/path/to/your/generated/results"
output_dir = "/path/to/your/output"

# Blender executable and script path
blender_path = "/path/to/blender-3.2.2-linux-x64/blender"
blender_script = "blender_script.py"

# Loop over subdirectories in the root directory
for sub_dir in sorted(os.listdir(root_dir)):
    sub_dir_path = os.path.join(root_dir, sub_dir)

    # Check if it's a directory
    if os.path.isdir(sub_dir_path):
        # Path to the .obj file
        obj_path = os.path.join(sub_dir_path, "/path/to/your/mesh.obj")
        # print(obj_path)
        # Check if the .obj file exists
        if os.path.exists(obj_path):
            # Absolute path of the .obj file
            absolute_obj_path = os.path.abspath(obj_path)

            # Output directory for this subdirectory
            output_dir = os.path.join(output_dir, sub_dir)

            # Create output directory if it doesn't exist
            os.makedirs(output_dir, exist_ok=True)

            # Construct the command to run Blender
            cmd = [
                blender_path, "-b", "-P", blender_script,
                "--", "--object_path", absolute_obj_path,
                "--output_dir", output_dir
            ]

            # Execute the command
            try:
                subprocess.run(cmd, check=True)
                print(f"Successfully processed {absolute_obj_path} for {sub_dir}")
            except subprocess.CalledProcessError as e:
                print(f"Error processing {absolute_obj_path} for {sub_dir}: {e}")
