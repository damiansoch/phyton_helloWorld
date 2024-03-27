import re


def is_email(email):
    # Simple regex pattern for validating an email address
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(pattern, email):
        return True
    else:
        return False


def register_user(email: str, age: int) -> str:
    if not isinstance(email, str):
        raise TypeError("Email has to be a string")

    if not is_email(email):
        raise ValueError("Email has to be a  valid email address")

    if not isinstance(age, int):
        raise TypeError("Age has to be an int")
    # register
    return f"User: {user_email} age: {user_age} registered"


user_email = "dsa@pl.pl"
user_age = 20
try:
    resp = register_user(user_email, user_age)
    print(resp)
except Exception as e:
    print(f"{type(e).__name__}: {e}")
print()


# task

def image_info(image: dict) -> str:
    if (image.get("image_id") is None) or (image.get("image_title") is None):
        raise TypeError('Keys "image_id" and "image_title" has to be provided')
    return f'Image {image.get("image_title")} has id {image.get("image_id")}'


image_dist = {
    "image_id": "5136",
    "image_title": "my cat"
}

try:
    resp = image_info(image_dist)
    print(resp)

except TypeError as e:
    print(f"{type(e).__name__}: {e}")
