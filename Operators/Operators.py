"""
Operators are used in expressions and each expression is evaluated to a specific value

+, -, *, /      -> ARITHMETIC
==, !=, <, >    -> COMPARISON
not, and, or, is, is not, in, not in    -> LOGICAL
=               -> ASSIGNMENT
"""

#  UNARY OPERATORS not success
success = False

if (not success):
    print("Didn't work")

#  BINARY OPERATORS -> just a normal ones with left and right operands
my_car = {
    "brand": "Toyota",
    "price": 10_000
}

print("brand" in my_car)
print("year" in my_car)
print("brand" not in my_car)

# task

set_1 = {1, 2, 3, 4}
set_2 = {1, 2, 3, 4}

print(set_1 == set_2)
print(set_1 is set_2)
print(set_1 is not set_2)

val1 = 4
val2 = 5

if val1 in set_1:
    print(f"{val1} present in set_1: {set_1}")
else:
    print(f"{val1} NOT present in set_1: {set_1}")

if val2 not in set_1:
    print(f"{val2} NOT present in set_1: {set_1}")
else:
    print(f"{val2} present in set_1: {set_1}")
