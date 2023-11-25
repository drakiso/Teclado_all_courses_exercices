""" Exercises Teclado https://teclado.com/30-days-of-python/python-30-day-29-decorators/"""

# Exercise 1
def double(func):
    def inner(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)

    return inner


# Exercise 2
books = []

def requires_content(func):
    def inner(*args, **kwargs):
        if books:
            return func(*args, **kwargs)

    return inner


# Exercise 3
def printer(func):
    def inner(*args, **kwargs):
        return_value = func(*args, **kwargs)

        if return_value is not None:
            print(return_value)

    return inner

