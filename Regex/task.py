# checking password
# >8 chars
# lowercase
# uppercase
# Number
# special symbol

import re

psw = ""
pattern = r"""
^(?=.*[a-z])       # At least one lowercase letter
(?=.*[A-Z])       # At least one uppercase letter
(?=.*\d)          # At least one digit
(?=.*[!@#$%^&*])  # At least one special character from the set provided
.{8,}             # At least 8 characters long
"""
compiled_pattern = re.compile(pattern, re.VERBOSE)
count = 0

while not compiled_pattern.match(psw):
    if count > 0:
        print(f"The password does not meet the criteria. {psw}")
    psw = input("please provide a password!:    ")
    count += 1
print(f"The password meets the criteria. {psw}")
