from typing import Type, List, Any


# iterate over dict, list, tuple, set, range, str

# -------------------------------------------for in

# task1
def convert_dict_to_list(dick_e: dict) -> list:
    list_of_tuples = list()

    for key, value in dick_e.items():
        new_value = value if isinstance(value, bool) else (value * 2 if isinstance(value, int) else value)
        key_value_tuple = (key, new_value)
        list_of_tuples.append(key_value_tuple)

    return list_of_tuples


dict1 = {'dtnsh': 20, 'crult': "carrot", 'pulrf': 87.5, 'phvvr': True, 'gbzzf': 'apple'}
dict2 = {'jedqa': "blue", 'fgevn': [1, 2, 3], 'fnhis': {'nested': 'dict'}, 'xklpb': False, 'loiqj': 58.2}
dict3 = {'ksubg': "text", 'yrbhx': (5, 6), 'nrurc': None, 'ybyvz': 50.0, 'dfaji': ['list', 'of', 'strings']}

list_from_dict1 = convert_dict_to_list(dict1)
list_from_dict2 = convert_dict_to_list(dict2)
list_from_dict3 = convert_dict_to_list(dict3)

print(list_from_dict1)
print(list_from_dict2)
print(list_from_dict3)


# task2

def filter_list_by_value_type(original_list: List[Any], value_type: Type[Any]) -> List[Any]:
    new_list = list()
    for el in original_list:
        if isinstance(el, bool) and value_type is int:
            continue
        if isinstance(el, value_type):
            new_list.append(el)
    return new_list


random_list1 = [(10, 4, 3), None, [3, 8, 6], 'SjbHk', False]
random_list2 = [(3, 4, 5), 17, {'q': 8, 'R': 7, 'p': 9}, 36.63581050823229, 'SGpvN']
random_list3 = [(8, 4, 2), None, 97.86395798316849, 93, 'gHtjs']

filtered_list_int_1 = filter_list_by_value_type(random_list1, type(None))
filtered_list_list_1 = filter_list_by_value_type(random_list1, list)
filtered_list_dict_2 = filter_list_by_value_type(random_list2, dict)
filtered_list_bool_3 = filter_list_by_value_type(random_list3, bool)
filtered_list_str_3 = filter_list_by_value_type(random_list3, str)

print(filtered_list_int_1)
print(filtered_list_list_1)
print(filtered_list_dict_2)
print(filtered_list_bool_3)
print(filtered_list_str_3)
print()
print("--------------------------------------------------------------------------")
# -------------------------------------------while
# task

user_answer = "yes"

while user_answer != "no":

    if user_answer != "yes":
        print(f"Your answer: \"{user_answer}\" is not a valid answer")
        continue
    try:
        first_user_input = float(input("Please enter the first number: "))

        while True:
            second_user_input = float(input("Please enter the second number: "))
            if second_user_input:
                break
            else:
                print("The divider can not be 0")

    except ValueError as e:
        print(f"This was not a number")
        continue

    print(
        f"The result of the division {first_user_input}/{second_user_input} "
        f"equals = {first_user_input / second_user_input}")

    print()

    user_answer = input("Do you want to continue? \"yes\" or \"no\": ")

print("Thank you")
