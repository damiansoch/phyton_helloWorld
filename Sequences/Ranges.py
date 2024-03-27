my_range = range(7)  # end {not included}
print(my_range)
range_list = list(my_range)
print(range_list)
print()

my_range_with_step = range(2, 20, 4)  # (start, end {not included}, step)
my_range_with_step_list = list(my_range_with_step)
print(my_range_with_step_list)
print(my_range_with_step_list[1])
print()

# using ranges in loops
for n in my_range_with_step:
    print(n)
