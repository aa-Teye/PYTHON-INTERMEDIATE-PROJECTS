import os
import shutil

def organize_folder(target_path):
    # Define file categories and their extensions
    extensions = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
        'Documents': ['.pdf', '.docx', '.doc', '.txt', '.xlsx', '.pptx'],
        'Videos': ['.mp4', '.mov', '.avi', '.mkv'],
        'Software': ['.exe', '.msi', '.apk'],
        'Archives': ['.zip', '.rar', '.7z']
    }

    # 1. Change directory to the target path
    if not os.path.exists(target_path):
        print(f"Error: Path {target_path} does not exist.")
        return

    os.chdir(target_path)

    # 2. Iterate through files
    for file in os.listdir():
        if os.path.isfile(file):
            filename, extension = os.path.splitext(file)
            extension = extension.lower()

            # 3. Find the correct folder for the extension
            moved = False
            for folder, ext_list in extensions.items():
                if extension in ext_list:
                    # Create folder if it doesn't exist
                    if not os.path.exists(folder):
                        os.makedirs(folder)
                    
                    # Move the file
                    shutil.move(file, os.path.join(folder, file))
                    print(f" Moved: {file} -> {folder}/")
                    moved = True
                    break
            
            if not moved:
                print(f"ℹ Skipped: {file} (Unknown Type)")

if __name__ == "__main__":
    print("--- Project 23: Automated File Organizer ---")
    # You can change this to any folder you want to clean up
    path_to_clean = input("Enter the full path of the folder to organize: ")
    organize_folder(path_to_clean)