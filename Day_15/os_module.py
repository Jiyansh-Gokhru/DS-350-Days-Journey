import os

# Current working directory
print("Current directory:", os.getcwd())

# List files in current directory
print("Files here:", os.listdir())

# Create a new folder
if not os.path.exists("new_folder"):
    os.mkdir("new_folder")
    print("Folder 'new_folder' created!")
else:
    print("'new_folder' already exists")