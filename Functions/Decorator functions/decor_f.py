# definition
def decorator_function(original_fn):
    def wrapper_function(*args, **kwargs):
        # Some actions before exec of the original_fn functions
        print("Executed before original_fn function")
        print(args)
        print(kwargs)

        result = original_fn(*args, **kwargs)
        # Some actions after exec of the original_fn functions
        print("Executed after original_fn function")

        return result

    return wrapper_function


@decorator_function
def my_function(*args, **kwargs):
    print("this is text from my_function")


my_function(10, name="Damian")
print("-------------------------------------------------------")


# example_1
def is_user_authenticated():
    print("getting the username of the user")
    username = "damiansoch"
    print(f"Checking if user: \"username: {username}\" authenticated")
    res = True
    if res:
        print("Authenticated")
    else:
        print("Not authenticated")
    return res


def check_user_authenticated(fn):
    def wrapper(*args, **kwargs):
        if is_user_authenticated():
            return fn(*args, **kwargs)
        else:
            raise Exception("User is not authenticated")

    return wrapper


@check_user_authenticated
def do_sensitive_job(a, b):
    # Perform action only if user authenticated
    print(f"a: {a}, b: {b}")
    print("Doing some sensitive job")


try:
    do_sensitive_job(5, 7)
    print("-----")
    do_sensitive_job(a=False, b=None)
except Exception as e:
    print(f"Error: {e}")
print("_________________________________________________")


# Example_2
def validate_inputs(fn):
    def wrapper(*args, **kwargs):
        if args:
            a, b = args
            if type(a) is int and type(b) is int:
                res = fn(*args, **kwargs)
                return res
            else:
                raise Exception("Validation error: a and b have to be a type of int")
        if kwargs:
            a, b = kwargs.values()
            if type(a) is int and type(b) is int:
                res = fn(*args, **kwargs)
                return res
            else:
                raise Exception("Validation error: a and b have to be a type of int")

    return wrapper


@validate_inputs
def sum_nums(a, b):
    return a + b


try:
    print(sum_nums(5, 8))
    print(sum_nums("5", 8))
except Exception as e:
    print(f"Error: {e}")
