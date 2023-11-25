""" Exercises Teclado https://teclado.com/30-days-of-python/python-30-day-11-sets/"""

# Exercise 1
s1 = set()

# Exercise 2
s1.update((1, 2, 3))

# Exercise 3
s2 = {3, 4, 5}

# Exercise 4
print(s1.union(s2))
print(s1.intersection(s2))
print(s1.difference(s2))
print(s1.symmetric_difference(s2))

# Exercise 5
guess_number = int(input("Enter a number:   "))

if guess_number in range(10):
    print(f"{guess_number} is within the range")
else:
    print(f"{guess_number} is not within the range")
