import os 
def move_file(source, destination):
    # Move by renaming (works inside same drive/disk)
    os.rename(source,destination)

def sort_files_by_extension(source_folder):
    if not os.path.isdir(source_folder):
        print(f"The folder {source_folder} does not exist.")
        return
    for filename in os.listdir(source_folder):
        file_path = os.path. join(source_folder, filename)

        if os.path.isfile(file_path):
            #extension
            parts = filename.rsplit('.', 1)
            if len(parts) == 2:
                extension == parts[1].lower()
            else:
                extension = 'no_extension'

            # create folder if it doesn't exist
            extension_folder = os.path.join(source_folder, extension)
            if not os.path.exists(extension_folder):
                os.mkdir(extension_folder)
            
            new_path = os.path.join(extension_folder, filename)
            move_file(file_path, new_path)

    print(f"Files have been stored in '{source_folder}'.")
if __name__ == "__main__":
    folder_to_sort = input("Enter the path of the folder to sort:")
    sort_files_by_extension(folder_to_sort)
