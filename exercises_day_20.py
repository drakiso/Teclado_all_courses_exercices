""" Exercises Teclado https://teclado.com/30-days-of-python/python-30-day-18-imports/"""

from operator import methodcaller

# Exercise 1
humpty_dumpty = [
    "  Humpty Dumpty sat on a wall,  ",
    "Humpty Dumpty had a great fall;     ",
    "  All the king's horses and all the king's men ",
    "    Couldn't put Humpty together again."
]

humpty_dumpty = map(methodcaller("strip"), humpty_dumpty)

for line in humpty_dumpty:
    print(line)

# Exercise 2
names = ("bob", "Christopher", "Rachel", "MICHAEL", "jessika", "francine")

short_names = [name for name in names if len(name) < 8]

print(short_names)

# Exercise 3
positive_numbers = filter(lambda number: number >= 0, range(-5, 11))

for positive_number in positive_numbers:
    print(positive_number)
