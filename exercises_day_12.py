""" Exercises Teclado https://teclado.com/30-days-of-python/python-30-day-12-functions/"""

# Exercise 1
def add(a, b):
    return a+b


def substract(a, b):
    return a-b


def divide(a, b):
    if b == 0:
        return "This operation is not possible"
    else:
        return a/b


def multiply(a, b):
    return a*b


# Exercise 2
def print_show_info(show):
    print(f"{show['title']} ({show['initial_release']}) - {show['seasons']} seasons")


tv_show = {
    "title": "Breaking Bad",
    "seasons": 5,
    "initial_release": 2008
}

print_show_info(tv_show)

# Exercise 3
series = [
    {"title": "Breaking Bad", "seasons": 5, "initial_release": 2008},
    {"title": "Fargo", "seasons": 4, "initial_release": 2014},
    {"title": "Firefly", "seasons": 1, "initial_release": 2002},
    {"title": "Rick and Morty", "seasons": 4, "initial_release": 2013},
    {"title": "True Detective", "seasons": 3, "initial_release": 2014},
    {"title": "Westworld", "seasons": 3, "initial_release": 2016},
]

for show in series:
    print_show_info(show)


# Exercise 4
def palindrome(word):
    processed_word = word.strip().upper()
    reversed_word = processed_word[::-1]

    if reversed_word == processed_word:
        print(f"{word} is a palindrome")
    else:
        print(f"{word} isn't a palindrome")


palindrome("Hannah")
