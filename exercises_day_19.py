""" Exercises Teclado https://teclado.com/30-days-of-python/python-30-day-19-exception-handling/"""

# Exercise 1
grades = input("Enter a list of grades separated by commas: ").split(",")
grades = [grade.strip() for grade in grades]

try:
    grades = [int(grade) for grade in grades]
except TypeError:
    print("The values you entered cannot be converted")

# Exercise 2
# See correction

# Exercise 3
try:
    with open("data.txt", "r") as text_file:
        print(text_file.read())
except FileNotFoundError:
    print("Error: Couldn't find data.txt")
