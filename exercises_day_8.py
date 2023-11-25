""" Exercises Teclado https://teclado.com/30-days-of-python/python-30-day-8-while-loops/ """
import random

# Exercise 1
target_number = random.randint(1, 101)
guess_number = int(input("Enter a number between 1 and 100: "))

while target_number != guess_number:
    if guess_number > target_number:
        print("Too high")
    elif guess_number < target_number:
        print("Too low")

    guess_number = int(input("Enter a number between 1 and 100: "))

print("Well done")

# Exercise 2
for letter in "python":
    if letter == "o":
        continue

    print(letter)

# Exercise 3
for number in range(2, 101):
    for divisor in range(2, number):
        if number % divisor == 0:
            break
    else:
        print(number)
