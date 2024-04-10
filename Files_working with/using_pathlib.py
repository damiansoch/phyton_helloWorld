from pathlib import Path

file_path = Path("test.txt")

print([m for m in dir(file_path) if not m.startswith('_')])

# find path to current working dir
print(Path.cwd())

# create path

# Get the current working directory
cwd = Path.cwd()
# Define a new folder within the current working directory
new_folder = cwd / "new_folder"
# Create the new folder (if it doesn't already exist)
new_folder.mkdir(exist_ok=True)
# Define a new file within the newly created folder
new_file = new_folder / "new_file.txt"
# Create the new file and write some content to it
with new_file.open(mode="w", encoding="utf-8") as file:
    file.write("This is a test file.")
print(f"New file created at: {new_file}")

# list all files and folders

for f in Path(".").iterdir():
    print(f)
