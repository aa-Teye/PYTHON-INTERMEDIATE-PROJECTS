import os
import shutil

def organize_folder(target_path):
    os.chdir(target_path)
    for file in os.listdir():
        if os.path.isfile(file):
            ext = file.split('.')[-1].lower()
            if not os.path.exists(ext):
                os.makedirs(ext)
            shutil.move(file, f"{ext}/{file}")
            print(f"Organized: {file} into {ext}/ folder")

if __name__ == "__main__":
    path = input("Paste the path of the folder you want to clean up: ")
    if os.path.exists(path):
        organize_folder(path)
        print("Done! Your files are now distilled.")
    else:
        print("Path not found. Please check the address and try again.")
for file in os.listdir():
    if os.path.isfile(file):
        ext = file.split('.')[-1].lower()
        if not os.path.exists(ext):
            os.makedirs(ext)
        shutil.move(file, f"{ext}/{file}")
        print(f"Organized: {file} into {ext}/ folder")