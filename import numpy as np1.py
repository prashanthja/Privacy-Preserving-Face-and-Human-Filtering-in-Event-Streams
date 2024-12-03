import numpy as np
import h5py
import os
import time

# List of folder names (you want to process each of these folders)
folders_list = [
    "20211005_1", "20211006_0", "20211006_1", "20211007_0", "20211007_1", "20211007_2",
    "20211008_0", "20211008_1", "20211015_0", "20211015_1", "20211015_2", "20211019_0",
    "20211019_1", "20211019_2", "20211019_3", "20211020_0", "20211021_0", "20211022_0",
    "20211023_0", "20211025_0", "20211025_1", "20211028_0", "20211028_1", "20211029_0",
    "20211029_1", "20211031_0", "20211101_0", "20211102_0", "20211102_1", "20211102_2",
    "20211104_0", "20211104_1", "20211106_0", "20211118_1", "20211120_0", "20211123_0",
    "20211123_1", "20211123_2", "20211124_0"
]

# Base input and output directory paths
input_base_directory = '/media/airlab/AIRLab-HDD/train/'
output_base_directory = '/media/airlab/AIRLab-HDD/train/train/'

starting_unix_timestamp = time.time()

sequence_duration = 1.0
time_interval = sequence_duration / 208  

# Create output base directory if it does not exist
os.makedirs(output_base_directory, exist_ok=True)

# Iterate through each folder in the list
for folder_name in folders_list:
    input_directory = os.path.join(input_base_directory, folder_name)  # Define the input folder
    output_directory = os.path.join(output_base_directory, folder_name)  # Define the corresponding output folder

    # Create the output folder for this particular input folder if it does not exist
    os.makedirs(output_directory, exist_ok=True)

    # Iterate through the files in the current input folder
    for filename in os.listdir(input_directory):
        if filename.endswith(".h5"):  # Process only .h5 files
            file_path = os.path.join(input_directory, filename)
            
            # Define the output filename (with .txt extension)
            output_filename = f"{os.path.splitext(filename)[0]}.txt"
            output_path = os.path.join(output_directory, output_filename)

            # Open the output file for writing
            with open(output_path, "w") as f:
                with h5py.File(file_path, 'r') as h5_file:
                    data = h5_file['data']

                    # Process each frame in the data
                    for frame_index in range(data.shape[0]):
                        frame_timestamp = starting_unix_timestamp + (frame_index * time_interval)
                        
                        # Process both channels (polarity 1 and 0)
                        for channel_index, polarity in enumerate([1, 0]):
                            frame_data = data[frame_index, channel_index]
                            y_coords, x_coords = np.nonzero(frame_data)  # Get the non-zero coordinates
                            
                            # Write the x, y coordinates along with the timestamp and polarity to the output file
                            for x, y in zip(x_coords, y_coords):
                                f.write(f"{frame_timestamp:.6f} {x} {y} {polarity}\n")

            print(f"Processed {filename} in {folder_name} and saved to {output_filename}")
