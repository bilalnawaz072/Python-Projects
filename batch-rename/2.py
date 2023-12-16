import os

# Define a function to list all files in a specified directory.
def list_files(directory):
    """List all files in the specified directory.

    Args:
        directory (str): The path to the directory whose files should be listed.

    Returns:
        list: A list of filenames found in the directory.
    """
    try:
        # Using list comprehension to list files in the specified directory
        return [file for file in os.listdir(directory) if os.path.isfile(os.path.join(directory, file))]
    except FileNotFoundError:
        print(f"The directory {directory} does not exist.")
        return []

def rename_files_with_extension(directory, old_extension, new_extension):
    """Rename all files in the specified directory with a specific extension to a new extension.

    Args:
        directory (str): The path to the directory whose files should be renamed.
        old_extension (str): The current extension of the files to be renamed.
        new_extension (str): The new extension for the files after renaming.

    Returns:
        int: The count of files successfully renamed.
    """
    renamed_count = 0
    files = [file for file in os.listdir(directory) if file.endswith(old_extension)]
    
    for file in files:
        # Construct the full path to the file.
        old_path = os.path.join(directory, file)
        # Construct the new file name by replacing the old extension with the new one.
        new_file_name = file.replace(old_extension, new_extension)
        # Construct the new path to the renamed file.
        new_path = os.path.join(directory, new_file_name)
        # Rename the file.
        os.rename(old_path, new_path)
        renamed_count += 1
    
    return renamed_count

def user_interface():
    """User interface to get directory path and file extensions for renaming."""
    directory = input("Enter the path to the directory: ")
    old_extension = input("Enter the current extension of the files you wish to rename: ")
    new_extension = input("Enter the new extension for the files: ")
    
    # Perform file renaming operation and return the result
    renamed_count = rename_files_with_extension(directory, old_extension, new_extension)
    print(f"{renamed_count} files have been renamed from {old_extension} to {new_extension}.")

# Call the user interface function
user_interface()

