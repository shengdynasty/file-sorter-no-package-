import os 
def move_file(source, destination):
    # Move by renaming (works inside same drive/disk)
    os.rename(source,destination)

def sort_files_by_estension(source_folder):
    if not os.path.isdir(source_folder):
        print(f"The folder {source_folder} does not exist.")