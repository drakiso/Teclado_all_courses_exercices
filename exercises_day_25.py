""" Exercises Teclado https://teclado.com/30-days-of-python/python-30-day-25-idiomatic-python/"""
import string
from random import sample


# Exercise 1
name = input("Enter your name:  ").strip().title() or "World"

print(f"Hello, {name}")

# Exercise 2
def exclusively_ascii(word):
    for letter in word.replace(" ", ""):
        if letter not in string.ascii_letters:
            print(f"{word} don't contains exclusively ASCII letters")
            break

    else:
        print(f"{word} contains exclusively ASCII letters")

# Exercise 3
numbers = [sample(range(1, 101), 15) for _ in range(3)]

for number_set in numbers:
    number_set.sort(reverse=True)
    del number_set[5:]

print(numbers)

