import os
import shutil  # This line was missing previously!

def move_files_by_extension(source_folder, target_folder, extensions):
    try:
        # Print the absolute path of the source folder
        print(f"Checking source folder: {os.path.abspath(source_folder)}")
        
        # Validate source folder
        if not os.path.exists(source_folder):
            print(f"Error: Source folder '{source_folder}' does not exist.")
            return

        # Create the target folder if it doesn't exist
        if not os.path.exists(target_folder):
            os.makedirs(target_folder)
            print(f"Created target folder: {target_folder}")

        # Debug: List files in source folder
        print(f"Files in source folder '{source_folder}':")
        for file in os.listdir(source_folder):
            print(f"  - {file}")

        # Loop through the files in the source folder
        moved_files = 0
        for file in os.listdir(source_folder):
            source_path = os.path.join(source_folder, file)
            # Check if it's a file and matches any of the specified extensions
            if os.path.isfile(source_path):
                file_extension = os.path.splitext(file)[1].lower()
                if file_extension in [ext.lower().strip() for ext in extensions]:
                    target_path = os.path.join(target_folder, file)
                    shutil.move(source_path, target_path)
                    print(f"Moved: {file}")
                    moved_files += 1

        if moved_files == 0:
            print("No files found with the specified extensions.")
        else:
            print(f"Successfully moved {moved_files} file(s).")
    except Exception as e:
        print(f"An error occurred: {e}")

# Inputs
source_folder = input("Enter the source folder path: ").strip()
target_folder = input("Enter the target folder path: ").strip()
extensions = input("Enter file extensions to move (comma-separated, e.g., .txt,.jpg): ").strip().split(',')

# Run the function
move_files_by_extension(source_folder, target_folder, extensions)
