# all falsy
print(bool(0))
print(bool(0.0))
print(bool(0j))

print(bool(False))
print(bool(None))

print(bool({}))  # empty dict
print(bool([]))  # empty list
print(bool(()))  # empty tuple
print(bool(set()))  # empty set
print(bool(range(0)))  # empty range

print(bool(""))  # empty string

#  usage example
my_list = []
if my_list:
    print("list is not empty")
else:
    print("list is empty")
