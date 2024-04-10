import os

directory_path = "my_test_dir"

if not os.path.exists(directory_path):
    os.mkdir(directory_path)
    print("directory created: " + directory_path)
else:
    print("Directory exists")

# create path to the file
file_path = os.path.join(directory_path, "test_file.txt")
if not os.path.exists(file_path):
    # Create and open the file for writing ('w' mode)
    with open(file_path, 'w', encoding='utf-8') as file:
        # Write some content to the file
        file.write("This is a test file created using os module in Python.")

    print(f"File created at: {file_path}")
else:
    print("File exists")

# listing files in dir
files_in_dir = os.listdir(directory_path)
print(f"Files in the dir: {directory_path} : {files_in_dir}")

# remove dir
# if os.path.exists(file_path):
#     os.remove(file_path)
#     print("File removed")
