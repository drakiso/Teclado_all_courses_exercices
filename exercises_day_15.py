""" Exercises Teclado https://teclado.com/30-days-of-python/python-30-day-14-files/"""

# Exercise 1
numbers = [1, 2, 3, 4, 5]

squares = [number ** 2 for number in numbers]

# Exercise 2
movie = {
    "title": "thor: ragnarok",
    "director": "taika waititi",
    "producer": "kevin feige",
    "production_company": "marvel studios"
}

movie = {key: value.title() for key, value in movie.items()}
