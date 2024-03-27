# file not found error
try:
    file = open("fil.txt", "r")
except FileNotFoundError as e:
    print(f"{type(e).__name__}: {e}")
else:
    content = file.read()
    print(content)
finally:

    if "file" in globals() and file and not file.close():
        file.close()
        print("File was closed")
    else:
        print('No file in "globals", closing not necessary')
