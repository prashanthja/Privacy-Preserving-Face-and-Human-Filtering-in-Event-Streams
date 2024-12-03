import re

# Read the list of filenames from a text file
with open('/media/lab_user/AIRLab-HDD/FES/train/train_list.txt', 'r') as file:
    filenames = file.readlines()

# Remove any extra spaces or newlines from each filename
filenames = [filename.strip() for filename in filenames]

# Group filenames by the numeric prefix (before the underscore)
file_groups = {}

# Group filenames by prefix (the part before the first underscore)
for filename in filenames:
    prefix = filename.split('_')[0]  # Get the prefix (before underscore)
    if prefix not in file_groups:
        file_groups[prefix] = []
    file_groups[prefix].append(filename)

# Sort the prefixes to process in order (e.g., '02', '05', '06', ...)
sorted_prefixes = sorted(file_groups.keys())

# Initialize a variable to keep track of the sequential numbering
global_count = 1

# List to hold the modified filenames
modified_filenames = []

# For each group of filenames (sorted by prefix)
for prefix in sorted_prefixes:
    group = file_groups[prefix]
    
    # Format the label for the current group
    label = f"{global_count:03d}"  # Ensure the label is 3 digits, e.g., 001, 002, ...
    
    # For each file in the group, update its filename with the current label
    for filename in group:
        # Modify the filename by appending the label
        new_filename = filename + " " + label 
        
        # Add the modified filename to the result list
        modified_filenames.append(new_filename)
    
    # Increment the global count for the next group
    global_count += 1

# Write the modified filenames back to the file
with open('/media/lab_user/AIRLab-HDD/train/modified_filenames.txt', 'w') as file:
    for filename in modified_filenames:
        file.write(f"{filename}\n")

# Optionally print the modified filenames
for filename in modified_filenames:
    print(filename)
