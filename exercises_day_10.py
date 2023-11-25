""" Exercises Teclado https://teclado.com/30-days-of-python/python-30-day-10-dictionaries/"""

# Exercise 1
album = {
    "title": "The Dark Side of the Moon",
    "artist": "Pink Floyd",
    "year": 1973,
    "tracks": (
        "Speak to Me",
        "Breathe",
        "On the Run",
        "Time",
        "The Great Gig in the Sky",
        "Money",
        "Us and Them",
        "Any Colour You Like",
        "Brain Damage",
        "Eclipse"
    )
}

# Exercise 2
for key, value in album.items():
    print(f"{key}: {value}")

# Exercise 3
del album["tracks"]
del album["year"]

album["date_of_release"] = "March 1st, 1973"

# Exercise 4
print(album.get("year"))
