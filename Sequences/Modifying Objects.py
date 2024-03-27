from copy import deepcopy

info = {
    "name": "Damian",
    "surname": "Socha",
    "reviews": []
}

info_copy = deepcopy(info)

info_copy["reviews"].append("Great course")

print(info)
print(info_copy)
