# They are similar to list, but Unordered, Unindexable, Duplicates Not Allowed, {}
# if duplicates found when creating set, the duplicates are removed

# -----Methods

# add, remove(when element not present produces error), discard(no error), copy


my_set = {1, 2, 3, 4}
other_set = {2, 4, 6, 8}
subset_set = {2, 4}

# union ->  new set with elements from both s and t
# all_ints = my_set.union(other_set) # we can pass list or tuple there, doesn't have to be set
all_ints = my_set | other_set
print(all_ints)
print()

# intersection -> new set with elements common to s and t
# common_s = my_set.intersection(other_set)
common_s = my_set & other_set
print(common_s)
print()

# issubset -> test whether every element in s is in t
# is_subset = subset_set.issubset(my_set)
is_subset = subset_set <= my_set
print(is_subset)
print()

# issuperset -> test whether every element in t is in s
# is_superset = my_set.issuperset(subset_set)
is_superset = my_set >= subset_set
print(is_superset)
print()

# difference -> new set with elements in s but not in t
# difference = my_set.difference(other_set)
difference_s = my_set - other_set
print(difference_s)
print()

# symmetric_difference -> new set with elements in either s or t but not both
# symmetric_difference_s = my_set.symmetric_difference(other_set)
symmetric_difference_s = my_set ^ other_set
print(symmetric_difference_s)
print()

# --- TASK
my_int_set = {1, 3, 5, 7, 6, 8, 7}
my_int_set.add(77)
print(my_int_set)
my_other_int_set = {1, 7, 9, 10, 32, 55}
common_s_1 = my_other_int_set & my_int_set
common_list = list(common_s_1)
print(common_list)
