""" Exercises Teclado https://teclado.com/30-days-of-python/python-30-day-4-lists-tuples/ """

# Exercice 1
movies = [
    ("The Room", "Tommy Wiseau", "2003", "$6,000,000")
]

# Exercice 2
title = input("Enter a movie's title:   ").strip().title()
director = input("Enter the director's name of the movie:   ").strip().title()
release_year = int(input("Enter the release year of the movie:   ").strip().title())
budget = int(input("Enter a movie's budget:   ").strip().title())

# Exercice 3
movie = title, director, release_year, budget

# Exercice 4
print(f"{movie[0]} {movie[2]}")

# Exercice 5
movies.append(movie)

# Exercice 6
print(movies[0])
print(movies[1])

# Exercice 7
movies.pop(0)
