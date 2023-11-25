""" Exercises Teclado https://teclado.com/30-days-of-python/python-30-day-18-imports/"""

# exercise 1
number = input("Enter a number from 1 to 10:    ")

if number < 1 or number > 10:
    raise ValueError(f"{number} is out of the range")

# exercise 2
def divide(a, b):
    try:
        print(a/b)
    except ZeroDivisionError:
        print("Can't divide by zero")
    except TypeError:
        print("Both values must be numbers. Cannot divide {a} and {b}")
    except ArithmeticError:
        print("Could not complete the division. The numbers were likely too large")

# exercise 3
def log_exception(exception, fn, **kwargs):
    values = ", ".join(f"{key}={value!r}" for key, value in kwargs.items())

    with open("log.txt", "a") as log_file:
        log_file.write(f"Exception: {exception}, Function: {fn}, Values: {values}\n")

def itemgetter(collection, identifier):
    try:
        return collection[identifier]
    except (IndexError, KeyError, TypeError) as ex:
        log_exception(ex, "itemgetter", collection=collection, identifier=identifier)

        raise
