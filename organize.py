import os
import shutil

def organize_files_by_extension(source_folder, extensions):
    try:
        # Check if the source folder exists
        if not os.path.exists(source_folder):
            print(f"Error: Source folder '{source_folder}' does not exist.")
            return

        # Process each extension provided by the user
        for ext in extensions:
            # Create a folder for the extension (without the dot)
            folder_name = ext.lstrip('.').upper() + "_Files"
            folder_path = os.path.join(source_folder, folder_name)

            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
                print(f"Created folder: {folder_path}")
            
            # Move files with the current extension to the folder
            files_moved = 0
            for file in os.listdir(source_folder):
                if os.path.isfile(os.path.join(source_folder, file)):
                    if file.lower().endswith(ext.lower().strip()):
                        shutil.move(os.path.join(source_folder, file), folder_path)
                        print(f"Moved: {file} -> {folder_path}")
                        files_moved += 1

            if files_moved == 0:
                print(f"No files with the extension '{ext}' found.")
        
        print("Organizing complete!")
    
    except Exception as e:
        print(f"An error occurred: {e}")

# Inputs
source_folder = input("Enter the source folder path: ").strip()
extensions = input("Enter file extensions to organize (comma-separated, e.g., .txt,.zip,.jpg): ").strip().split(',')

# Run the function
organize_files_by_extension(source_folder, extensions)
