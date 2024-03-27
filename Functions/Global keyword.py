a = 15


def my_fn():
    global a
    a += 1


my_fn()

print(a)
