# Copying

my_list = [1, 2, 3, None]
copy_of_my_list = my_list[:]
copy_of_my_list_1 = list(my_list)
copy_of_my_list_2 = my_list.copy()

copy_of_my_list.append(None)

print(my_list)
print(copy_of_my_list)
print(my_list == copy_of_my_list)
print(id(my_list) == id(copy_of_my_list))

print()

# Task 1

created_list = [1, None, False, "yes", 0]
print(created_list)
created_list.pop(2)
print(created_list)
print(len(created_list))
created_list.reverse()
print(created_list)
another_list = [2, 4]
created_list += another_list
print(created_list)

print()

# Task 2

list_one = [1, 2, 3]
list_two = [4, 5, 6]
list_whole = list_one + list_two
merged_list = list_one.__add__(list_two)
print(list_whole)
print(merged_list)

# zip

fruits = ["apples", "bananas", "limes"]
quantities = [10, 20, 15]
fruit_qtys_zip = zip(fruits, quantities)
print(fruit_qtys_zip)
# The zip function returns an iterator, and once an iterator is consumed, it cannot be reused or reset.
# print(list(fruit_qtys_zip))
print(dict(fruit_qtys_zip))

fruit_qtys_zip = zip(fruits, quantities)
for fruit, qty in fruit_qtys_zip:
    print(f"{qty} {fruit}/s")
