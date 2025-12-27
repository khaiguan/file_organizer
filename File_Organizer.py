import os
import shutil

source_dir = r"C:\Users\User\Downloads"

extensions = {
    'Screenshots': ['.png'],
    'Images': ['.jpg', '.jpeg', '.webp', '.heic'],
    'Videos': ['.mp4', '.mov', '.avi', '.mkv'],
    'PDFs': ['.pdf', '.epub'],
    'Word Document': ['.docx', '.doc'],
    'Slides': ['.pptx', '.ppt'],
    'Excel Sheet': ['.csv', '.xlsx'],
    'Songs': ['.mp3', '.flac'],
    'Text': ['.txt'],
    'Scripts': ['.ipynb']
}

def sort_files():
    # Change directory to the source
    if not os.path.exists(source_dir):
        print(f"Error: The folder '{source_dir}' was not found.")
        return

    os.chdir(source_dir)

    for file in os.listdir():
        # Skip directories, we only want files
        if os.path.isdir(file):
            continue

        # Get the file extension and convert to lowercase
        name, ext = os.path.splitext(file)
        ext = ext.lower()

        # Move the file based on its extension
        for folder_name, ext_list in extensions.items():
            if ext in ext_list:
                # Create the folder if it doesn't exist
                if not os.path.exists(folder_name):
                    os.makedirs(folder_name)
                
                # Move the file
                print(f"Moving {file} to {folder_name}...")
                shutil.move(file, os.path.join(folder_name, file))
                break

if __name__ == "__main__":
    sort_files()
    print("Sorting complete!")

    quit()
