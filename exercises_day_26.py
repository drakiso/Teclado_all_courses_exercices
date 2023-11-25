""" Exercises Teclado https://teclado.com/30-days-of-python/python-30-day-26-standard-library/"""
from collections import namedtuple, defaultdict
from operator import mul
from functools import partial


# exercise 1
Movie = namedtuple("Movie", ["title", "director", "year", "budget"])

title = input("Enter a movie's title:   ")
director = input("Enter the movie's director:   ")
year = int(input("Enter the movie's year of release:   "))
budget = int(input("Enter a movie's title:   "))

movie = Movie(title=title, director=director, year=year, budget=budget)

# exercise 2
character_count = defaultdict(int)
list_character = "onomatopoeia"

for character in list_character:
    character_count[character] += 1

print(max(character_count, key=lambda key: character_count[key]))

# exercise 3
double = partial(mul, 2)

# exercise 4
read = partial(open, mode="r")
