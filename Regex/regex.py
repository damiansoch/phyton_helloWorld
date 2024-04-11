import re

# search -> search for string in string
print("__________________________")
print("search")

my_string = "my name si Damian"
res = re.search(r"D....n", my_string)
print(res)
my_pattern = re.compile(r"D....n")
print(my_pattern)
print(my_pattern.search(my_string))  # <re.Match object; span=(11, 17), match='Damian'>

# match -> matches the beginning of the string
print("__________________________")
print("match")
print(my_pattern.match(my_string))  # None
print(my_pattern.match("Damian"))  # <re.Match object; span=(0, 6), match='Damian'>
print(my_pattern.match("D0213n isjkdflskafj"))  # <re.Match object; span=(0, 6), match='D0213n'>

# fullmatch -> matches whole string
print("__________________________")
print("fullmatch")
print(my_pattern.fullmatch(my_string))  # None
print(my_pattern.fullmatch("Damian"))  # <re.Match object; span=(0, 6), match='Damian'>
print(my_pattern.fullmatch("D0213n isjkdflskafj"))  # None

# findall -> matches whole string
print("__________________________")
print("findall")
print(my_pattern.findall("Damian is the best Damian"))
print(len(my_pattern.findall("Damian is the best Damian")))
