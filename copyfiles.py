import shutil
import os

def copy_files_from_subfolders(parent_dir, dest_dir):
    # Ensure the destination directory exists, if not, create it
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)


    # Loop over each source directory

    for src_dir in src_dirs:
        # Iterate over all files in the source directory
        for filename in os.listdir(src_dir):
            # Full path to the source file
            src_file = os.path.join(src_dir, filename)

            # Check if it's a file (not a directory) before copying
            if os.path.isfile(src_file):
                # Full path to the destination file
                dest_file = os.path.join(dest_dir, filename)

                # If a file with the same name already exists in the destination, rename it
                if os.path.exists(dest_file):
                    # Create a unique name for the file (appending a number)
                    name, ext = os.path.splitext(filename)
                    i = 1
                    while os.path.exists(dest_file):
                        dest_file = os.path.join(dest_dir, f"{name}_{i}{ext}")
                        i += 1

                # Copy the file to the destination directory
                shutil.copy(src_file, dest_file)
                print(f"Copied {filename} from {src_dir} to {dest_dir}")
# Example usage:
parent_folder = '/media/airlab/AIRLab-HDD/train'
dest_folder = '/media/airlab/AIRLab-HDD/train/train1'

copy_files_from_subfolders(parent_folder, dest_folder)
