import os

# Define the directory containing the files you want to rename.
directory = "d:/Bilal Work/Current Project/ruff/Python Projects/batch-rename/bilal"

# List of all files in the directory.
files = os.listdir(directory)
# print(files)

# Loop through each file in the directory.
old_name = ".ts"
new_name = ".py"

for file in files:

    # Construct the full path to the file.
    old_path = os.path.join(directory, file)

    # Construct the new path to the renamed file.
    new_path = os.path.join(directory, file.replace(old_name, new_name))

    # Rename the file.
    os.rename(old_path, new_path)

# print out the old and new file names to verify the changes.
print("Old file name: " + old_name)
print("New file name: " + new_name)