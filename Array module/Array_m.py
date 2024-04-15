from array import array

my_int_array = array("i", [10, 4, 6, 8, 9, 6, 15])
print(my_int_array)
print(type(my_int_array))
print(dir(my_int_array))

# saving arrays as .bin file
with open("my array.bin", "wb") as file:
    my_int_array.tofile(file)

# reading form this file
imported_array = array("i")

with open("my array.bin", "rb") as file:
    imported_array.fromfile(file, 3)

print(imported_array)
