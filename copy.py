import os
import shutil

def copy_files_from_multiple_sources(src_folders, dest_folder):
   

    # Loop through each source folder
    for src_folder in src_folders:
        if os.path.exists(src_folder):
            print(f"Copying files from: {src_folder}")
            # Iterate over all files in the source folder
            for filename in os.listdir(src_folder):
                # Construct full file path
                src_file = os.path.join(src_folder, filename)
                dest_file = os.path.join(dest_folder, filename)
                
                # Check if it's a file (and not a subdirectory)
                if os.path.isfile(src_file):
                    try:
                        # Copy the file to the destination folder
                        shutil.copy(src_file, dest_file)
                        print(f"Copied: {filename}")
                    except Exception as e:
                        print(f"Error copying {filename}: {e}")
        else:
            print(f"Source folder does not exist: {src_folder}")

# Example usage with your folders_list
folders_list = [
    "20211006_0", "20211006_1", "20211007_0", "20211007_1", "20211007_2",
    "20211008_0", "20211008_1", "20211015_0", "20211015_1", "20211015_2", "20211019_0",
    "20211019_1", "20211019_2", "20211019_3", "20211020_0", "20211021_0", "20211022_0",
    "20211023_0", "20211025_0", "20211025_1", "20211028_0", "20211028_1", "20211029_0",
    "20211029_1", "20211031_0", "20211101_0", "20211102_0", "20211102_1", "20211102_2",
    "20211104_0", "20211104_1", "20211106_0", "20211118_1", "20211120_0", "20211123_0",
    "20211123_1", "20211123_2", "20211124_0"
]

dest_folder = '/media/airlab/AIRLab-HDD/train/train/'  # Replace with your actual destination folder path

# Convert folder names to full paths if required (optional)
src_folders = [os.path.join('/media/airlab/AIRLab-HDD/train/train/', folder) for folder in folders_list]

copy_files_from_multiple_sources(src_folders, dest_folder)
