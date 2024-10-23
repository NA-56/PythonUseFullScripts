import os

# Set the path to the folder containing the JPEG images
folder_path = r"path_folder"

# Loop through all files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith(".jpeg"):  # Only target .jpeg files
        # Remove the first 9 characters from the filename
        new_filename = filename[9:]
        
        # Build full file paths
        old_file = os.path.join(folder_path, filename)
        new_file = os.path.join(folder_path, new_filename)
        
        # Rename the file
        os.rename(old_file, new_file)
        print(f"Renamed: {filename} -> {new_filename}")

print("Renaming completed.")
