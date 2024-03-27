# Tuple or list (arg)
def sum_nums(*args):
    my_list = list(args)
    print(my_list)
    my_list.sort(reverse=False, key=None)
    print(my_list)
    print(type(args))
    return sum(args)


my_sum = sum_nums(8, 4, 6, )
print(my_sum)
print()


# Dict (kwarg)
def get_post_info(**kwargs):
    print(type(kwargs))
    print(kwargs)


get_post_info(name="Damian", posts=25)  # Have to use the named parameters for this to work
print()


def setup_db_connection(hostname: str, port: int, username: str, password: str, **kwargs) -> str:
    print(f"not used parameters: {kwargs}")
    return (f""
            f"hostname is {hostname}, "
            f"port is {port}, "
            f"username is {username}, "
            f"password is {password}")


data = {
    "hostname": "localhost",
    "username": "damiansoch",
    "password": "dsa1",
    "port": 4005,
    "other": "other_value",
    "other1": "other_value1",
}

res = setup_db_connection(hostname=data.get("hostname"), port=data.get("port"), username=data.get("username"),
                          password=data.get("password"))
res1 = setup_db_connection(**data)  # object keys names has to be the same as args in the function
print(res)
print(res1)
print()
