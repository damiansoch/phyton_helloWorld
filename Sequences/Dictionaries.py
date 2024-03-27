my_car = {
    "brand": "BMW",
    "price": 40_000
}

print(my_car["brand"])
print()

dict_keys = list(my_car.keys())

print(dict_keys)
print(type(dict_keys))

# accessing not present key
# print(my_car["model"])  # this will throw an error
print(my_car.get("model"))  # this will print None
print(my_car.get("model", "unavailable"))  # this will print unavailable in None

# convert list to dict
my_list = [["a", 10], ["b", 20]]  # list of lists
print(dict(my_list))
print()

my_list_of_tuples = [("a", 10), ["b", 20]]  # list of tuples (mixed ith list of lists)
print(dict(my_list_of_tuples))
print()

# task
my_dict = dict()

key_1 = input("enter first key: ")
value_1 = input(f"enter  value for the key {key_1}: ")
my_dict[key_1] = value_1
print()

key_2 = input("enter second key: ")
value_2 = input(f"enter  value for the key {key_2}: ")
my_dict[key_2] = value_2
print()

key_3 = input("enter third key: ")
value_3 = input(f"enter  value for the key {key_3}: ")
my_dict[key_3] = value_3
print()

print(my_dict)

# deleting the key
del my_dict[key_2]
print(my_dict)
