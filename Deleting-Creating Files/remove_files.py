import os
from pathlib import Path

def remove_files_by_extension(folder_path, extension, dry_run=True):
    """
    Remove all files with a specific extension from a folder and its subfolders.
    
    Args:
        folder_path (str): Path to the folder to clean
        extension (str): File extension to remove (with or without dot)
        dry_run (bool): If True, only prints files that would be removed without actually removing them
    
    Returns:
        tuple: (number of files removed, total size freed in bytes)
    """
    # Ensure extension starts with dot and remove any spaces
    if not extension.startswith('.'):
        extension = '.' + extension
    extension = extension.strip()
    
    # Convert to Path object
    folder_path = Path(folder_path)
    
    if not folder_path.exists():
        raise ValueError(f"Folder path does not exist: {folder_path}")
    
    files_removed = 0
    total_size = 0
    
    # Walk through all files and subfolders
    for file_path in folder_path.rglob(f"*{extension}"):
        try:
            file_size = file_path.stat().st_size
            if dry_run:
                print(f"Would remove: {file_path} ({file_size:,} bytes)")
            else:
                print(f"Removing: {file_path} ({file_size:,} bytes)")
                file_path.unlink()
            
            files_removed += 1
            total_size += file_size
            
        except Exception as e:
            print(f"Error processing {file_path}: {e}")
    
    return files_removed, total_size

# Configuration
FOLDER_PATH = "C:/Users/YourUsername/Documents/TestFolder"  # Replace with your folder path
FILE_EXTENSION = ".txt"  # Replace with your desired extension

# First do a dry run to show what would be removed
print("\nDry run - files that would be removed:")
files_count, total_size = remove_files_by_extension(FOLDER_PATH, FILE_EXTENSION, dry_run=True)

if files_count == 0:
    print(f"\nNo files found with extension {FILE_EXTENSION}")
else:
    print(f"\nFound {files_count:,} files with extension {FILE_EXTENSION}")
    print(f"Total size: {total_size:,} bytes ({total_size / (1024*1024):.2f} MB)")
    
    # Perform actual deletion
    print("\nProceeding with deletion...")
    files_removed, size_freed = remove_files_by_extension(FOLDER_PATH, FILE_EXTENSION, dry_run=False)
    print(f"\nOperation completed:")
    print(f"Files removed: {files_removed:,}")
    print(f"Space freed: {size_freed:,} bytes ({size_freed / (1024*1024):.2f} MB)")