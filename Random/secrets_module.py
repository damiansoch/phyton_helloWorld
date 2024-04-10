import secrets
import string

# Generating passwords

digits = string.digits
ascii_letters = string.ascii_letters
punctuation = string.punctuation

all_chars = digits + ascii_letters + punctuation
print(all_chars)

psw = ""

invalid_chars = ["'", '"', ";", "\n", "\r", "\t"]


def contains_invalid_char(s):
    if any(char in s for char in invalid_chars):
        print(f"Password contains invalid characters. {psw}")
        return True
    print("No invalid chars in the password")
    return False


def contains_one_lowercase_one_uppercase_and_one_special_char(p: str) -> bool:
    if any(char in p for char in digits) and any(char in p for char in ascii_letters) and any(
            char in p for char in punctuation):
        print("Password have all required chars")
        return True
    print(f"Password does not have all required chars! {psw}")
    return False


while psw == "" or contains_invalid_char(psw) or not contains_one_lowercase_one_uppercase_and_one_special_char(psw):
    psw = ""  # Reset psw to empty
    for n in range(10):
        symbol = secrets.choice(all_chars)
        psw += symbol

print(psw)

# Generating CSRF token -> session token
print("________________________________")
print("Generating CSRF token")
token = secrets.token_hex(128)
print(token)

# Generating authentication token -> for reset password f.e.
print("________________________________")
print("Generating authentication token")
url_save_token = secrets.token_urlsafe(128)
print(url_save_token)

# Generating single-use password -> for example to sent in mobile auth
print("________________________________")
print("Generating single-use password")
short_psw = "".join(secrets.choice(digits) for _ in range(6))
print(short_psw)
