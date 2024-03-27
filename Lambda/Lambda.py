def greeting(greet):
    return lambda name: f"{greet}, {name}!"


morning_greeting = greeting("Good morning")

print(morning_greeting("Damian"))

# sort list using lambda
my_list = [
    {"name": "John", "score": 20},
    {"name": "Damian", "score": 99},
    {"name": "Eoin", "score": 11},
    {"name": "Ann", "score": 55},
]

my_list.sort(key=lambda i: i["score"])

print(my_list)

my_list.sort(key=lambda i: i["name"], reverse=True)

print(my_list)
print()

# filtering list using lambda

new_list = list(filter(lambda i: i.get("score") > 21, my_list))
print(new_list)
