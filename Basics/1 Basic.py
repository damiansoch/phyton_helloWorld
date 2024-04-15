"""

print("Hello python"),
print("Damian"),
print(-20)

print(True)
print([1, 2, "damian"])

print({
    "min": 1,
    "max": 2,
    "name": "Damian"
})


# build in functions
print
# creating functions


def my_fn(a, b=0):
    s = a + b
    return s


def greetings(person_name):
    print("Hello " + person_name)


print(my_fn(2, 4))
print(my_fn(5))

print(print)

name = input("Enter your name: ")

greetings(name)

print(dir(int))
print()



print(dir())
print(__name__)

"""


def can_be_parsed_to_int(s):
    try:
        # Attempt to convert the string to an integer
        int(s)
        return True
    except ValueError:
        # If a ValueError is raised, the conversion failed
        return False


favorite_number = input("Please enter your favorite number, and i will double it: ")

if not can_be_parsed_to_int(favorite_number):
    print("This was not a number")
else:
    fav_num_int = int(favorite_number)
    print(fav_num_int * 2)
    print(id(favorite_number))
