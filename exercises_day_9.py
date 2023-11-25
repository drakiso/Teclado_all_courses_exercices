""" Exercises Teclado https://teclado.com/30-days-of-python/python-30-day-9-enumerate-zip/ """

# Exercise 1
main_characters = [
    ("BoJack Horseman", "Will Arnett", "Horse"),
    ("Princess Carolyn", "Amy Sedaris", "Cat"),
    ("Diane Nguyen", "Alison Brie", "Human"),
    ("Mr. Peanutbutter", "Paul F. Tompkins", "Dog"),
    ("Todd Chavez", "Aaron Paul", "Human")
]

for name, voice, specy in main_characters:
    print(f"{name} is a {specy.lower()} voiced by {voice}")


# Exercise 2
student_name, student_id, (major, minor) = ("John Smith", 11743, ("Computer Science", "Mathematics"))

