import random

# float
print(random.random())
# for f in dir(random):
#     if not f.startswith("-"):
#         print(f)
print(" ".join(f for f in dir(random) if not f.startswith("_")))
print(random.uniform(10, 10.1))

# int
print(random.randint(0, 9))

# shuffle
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
random.shuffle(my_list)
print(my_list)

# choice (select random item from the sequence)
print(random.choice(my_list))

# choices (non unique)
print(random.choices(my_list, k=2))
# generate password from username mixed with some numbers and chars length 15 (not recommended)
username = "damiansoch"
other_charsToUse = "1234567890!£$%^&*()"
psw_list = random.choices(username + other_charsToUse, k=15)
psw = "".join(psw_list)
print(psw)

# sample (unique)
print(random.sample(my_list, k=7))
# selecting numbers fro a big range
print(random.sample(range(100_000_000), k=5))
