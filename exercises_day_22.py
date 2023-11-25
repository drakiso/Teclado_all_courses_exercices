""" Exercises Teclado https://teclado.com/30-days-of-python/python-30-day-18-imports/"""

from itertools import cycle


# exercise 1
numbers = [(23, 3, 56), (98, 1034, 54), (254, 344, 5), (45, 2), (122, 63, 74)]

sum_numbers = map(sum, numbers)

# exercise 2
days = cycle(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
employees = cycle(['A', 'B', 'C'])

for number in range(1,31):
    print(f"day {number} ({next(days)}): {next(employees)} close the shop")

