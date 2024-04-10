import pathlib
from zipfile import ZipFile

# Create a Path object for the directory
dir_path = pathlib.Path("Zip_archives_test")
# Ensure the directory exists
dir_path.mkdir(parents=True, exist_ok=True)

# Create Path objects for the files within the directory
file_path = dir_path / "first.txt"
file_path2 = dir_path / "second.txt"

# Writing text to the first file
file_path.write_text(
    "Hello, World!\nThis is a sample text file.\nIt contains a few lines of text for demonstration purposes.\n",
    encoding="utf-8")

print(f"File written at: {file_path}")

# Writing text to the second file
file_path2.write_text(
    "Hello, World!\nThis is a second text file.\nIt contains a few lines of text for demonstration purposes again.\n",
    encoding="utf-8")

print(f"File written at: {file_path2}")

# zipping the file
zip_path = dir_path.with_suffix(".zip")

with ZipFile(zip_path, "w") as zipf:
    for file in dir_path.iterdir():
        zipf.write(file, arcname=file.relative_to(dir_path.parent))
print(f"Directory zipped into: {zip_path}")

# reading zip file
# Path for the directory where you want to extract the zip file
extract_dir_path = pathlib.Path("Zip_archives_test_extracted")
# Ensure the extract directory exists
extract_dir_path.mkdir(parents=True, exist_ok=True)
# Extracting the zip file
with ZipFile(zip_path, 'r') as zipf:
    zipf.extractall(extract_dir_path)
print(f"Contents extracted to: {extract_dir_path}")
