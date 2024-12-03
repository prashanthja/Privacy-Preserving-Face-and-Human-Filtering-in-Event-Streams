import os

# Define the directory where your files are located
directory = '/media/lab_user/AIRLab-HDD/train/train'  # Change this to your folder path

# Define the path where you want to save the output text file
output_file = '/media/lab_user/AIRLab-HDD/train/filenames.txt'  # Change this to your desired location

# Ensure the output directory exists, create it if it doesn't
output_dir = os.path.dirname(output_file)
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Open a text file to write the file names
with open(output_file, 'w') as file:
    # Iterate through the directory and list all files
    for filename in os.listdir(directory):
        full_path = os.path.join(directory, filename)
        # If it's a file (and not a directory), write it to the file
        if os.path.isfile(full_path):
            file.write(filename + '\n')

print(f"File names have been written to '{output_file}'.")
