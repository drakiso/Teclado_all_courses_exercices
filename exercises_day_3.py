""" Exercises Teclado https://teclado.com/30-days-of-python/python-30-day-3-string-formatting/ """

# Exercise 1
greeting = "Hello, world"

print("{}!".format(greeting))

# Exercise 2
name = input("Enter your name:  ").strip().title()

print(f"Hello, {name}!")

# Exercise 3
print("I am " + str(29))

# Exercise 4
title = "Joker"
director = "Todd Phillips"
release_year = 2019

print("{} ({}), directed by {}".format(title, release_year, director))
