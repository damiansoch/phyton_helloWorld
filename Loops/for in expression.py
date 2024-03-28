# Expression for Element in Sequence if Condition(optional)
from typing import List

all_nums = [78, -68, 99, -100, -52, 88, -80, -94, -70, 82]

# normally
absolute_numbers = []
for num in all_nums:
    absolute_numbers.append(abs(num))

# list comprehension
absolute_numbers_2 = [abs(num) for num in all_nums]  # [] -> because we want a list
positive_numbers_only = [num for num in all_nums if num > 0]

print(all_nums)
print(absolute_numbers)
print(absolute_numbers_2)
print(positive_numbers_only)

# set comprehension
my_set = {1, 20, 15}

new_set = {val * val for val in my_set}

print(my_set)
print(new_set)

# dict comprehension

my_dict = {
    'key_0': 'string value',  # String
    'key_1': [1, 2, 3],  # List
    'key_2': 3.14,  # Float
    'key_3': True,  # Boolean
    'key_4': None,  # NoneType
    'key_5': -44,  # Int
    'key_6': -64,  # Int
    'key_7': 37,  # Int
    'key_8': -66,  # Int
    'key_9': 79  # Int
}

newDict = {key: value * 10 for key, value in my_dict.items() if not isinstance(value, bool) and isinstance(value, int)}

print(my_dict)
print(newDict)

# two lists to dict
grades = (80, 95, 48)
subjects = ["math", "science", "PI"]

print(dict(zip(subjects, grades)))

subject_grades = {subject: grade - 10 for subject, grade in zip(subjects, grades)}
print(subject_grades)


# task1
def convert_dict_values_to_upper(orig_dict: dict) -> dict:
    new_dict = {key: value.upper() for key, value in orig_dict.items()}
    return new_dict


person = {
    'name': 'John Doe',
    'age': '30',
    'city': 'New York',
    'occupation': 'Software Developer',
    'hobby': 'Photography'
}

converted_person = convert_dict_values_to_upper(person)
print(converted_person)

# task2
items = [
    "apple", "banana", "cherry", "date", "elderberry",
    "fig", "grape", "honeydew", "kiwi", "lemon",
    "mango", "nectarine", "orange", "papaya", "quince",
    "raspberry", "strawberry", "tangerine", "ugli fruit", "watermelon",
    "xigua", "yellow watermelon", "zucchini"
]

new_items = list(reversed([el for el in items if len(el) > 5]))
print(items)
print(new_items)

# task2

list_1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12],
    [13, 14, 15]
]

unnested_list = [num for sublist in list_1 for num in sublist]
print(unnested_list)
