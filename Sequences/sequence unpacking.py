# we can perform unpacking on list or tuples because they are ordered

random_fruits = (
    'Raspberry',
    'Watermelon',
    'Elderberry',
)
fruit1, fruit2, fruit3 = random_fruits

print(fruit1)
print(fruit2)
print(fruit3)
print()

fruit1, *remaining_fruits = random_fruits
print(fruit1)
print(remaining_fruits)
print(type(remaining_fruits))
print()

# unpacking the dictionary into keyword arguments
user_profile = {
    "name": "Bogdan",
    "comments_qty": 23
}

user_data = ["Damian", 33]


def user_info(name, comments_qty=0):
    if not comments_qty:
        return f"{name} has no comments"

    return f"{name} has {comments_qty} comments"


print(user_info(**user_profile))  # unpacking the dictionary into keyword arguments

print(user_info(*user_data))  # unpacking the list into positional arguments

# omitting element when unpacking
comment = ("Great course", "bob_202", 120, 4.7)

_, username, _, rating = comment
print(username)
print(rating)
print()

# creating new dictionary by unpacking other dictionary
button = {
    "width": 150,
    "text": "buy",
    "color": "white"
}
red_button = {
    **button,
    "color": "red",
    "border": True
}
print(red_button)
print()
