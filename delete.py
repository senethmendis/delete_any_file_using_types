import os

def delete_files_by_extension(directory, extension, recursive=False):
    """
    Delete files with a given extension in the specified directory.
    
    :param directory: Path to the folder where files should be deleted
    :param extension: File extension to delete (e.g., ".JPG", ".AAE")
    :param recursive: If True, search in subdirectories as well
    """
    # Ensure extension starts with a dot
    if not extension.startswith("."):
        extension = "." + extension
    
    deleted_files = []
    
    if recursive:
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.lower().endswith(extension.lower()):
                    file_path = os.path.join(root, file)
                    try:
                        os.remove(file_path)
                        deleted_files.append(file_path)
                        print(f"Deleted: {file_path}")
                    except Exception as e:
                        print(f"Error deleting {file_path}: {e}")
    else:
        for file in os.listdir(directory):
            file_path = os.path.join(directory, file)
            if os.path.isfile(file_path) and file.lower().endswith(extension.lower()):
                try:
                    os.remove(file_path)
                    deleted_files.append(file_path)
                    print(f"Deleted: {file_path}")
                except Exception as e:
                    print(f"Error deleting {file_path}: {e}")
    
    print(f"\nTotal files deleted: {len(deleted_files)}")


# Example usage:
# delete_files_by_extension("C:/Users/YourName/Pictures", ".AAE", recursive=True)
delete_files_by_extension(r"D:\Pictures\iPHONE UPACK\video\2025-08-02", ".AAE", recursive=False)
