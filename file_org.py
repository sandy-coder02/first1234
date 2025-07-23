import os
import shutil

# Define categories based on file extensions
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Audio": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
    "Executables": [".exe", ".msi", ".sh", ".bat"],
}

def organize_files(directory):
    if not os.path.exists(directory):
        print("Directory does not exist!")
        return
    
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        
        if os.path.isfile(file_path):  # Check if it's a file
            file_extension = os.path.splitext(filename)[1].lower()
            
            # Find the category for the file
            for category, extensions in FILE_CATEGORIES.items():
                if file_extension in extensions:
                    category_path = os.path.join(directory, category)
                    
                    if not os.path.exists(category_path):
                        os.makedirs(category_path)
                    
                    shutil.move(file_path, os.path.join(category_path, filename))
                    print(f"Moved {filename} to {category}/")
                    break
            else:
                # Move unrecognized files to "Others" folder
                other_path = os.path.join(directory, "Others")
                if not os.path.exists(other_path):
                    os.makedirs(other_path)
                shutil.move(file_path, os.path.join(other_path, filename))
                print(f"Moved {filename} to Others/")

if __name__ == "__main__":
    target_directory = input("Enter the directory path to organize: ")
    organize_files(target_directory)
    print("File organization complete!")
