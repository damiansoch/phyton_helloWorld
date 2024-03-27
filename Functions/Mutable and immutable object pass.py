# -------------------------immutable
def sum_nums(num1, num2):
    num1 = num1 + 1
    return num1 + num2


a = 3
b = 4

sum_ab = sum_nums(2, 3)
print(a)
print(b)
print(sum_ab)


# --------------------------mutable
def add_age(person):
    person_copy = person.copy()
    # need to copy the mutable object to avoid changing the original one
    person_copy["age"] += 1
    return person_copy


person1 = {
    "age": 21,
    "name": "Damian"
}

new_person = add_age(person1)

print(new_person)
print(person1)


# task

def convert_lists_to_dict(list1, list2):
    zip_obj = zip(list1, list2)
    my_dict_obj = dict(zip_obj)
    return my_dict_obj


peoples = ["Damian", "Adam", "Milena"]
ages = [39, 26, 15]

my_dict = convert_lists_to_dict(peoples, ages)
print(my_dict)
