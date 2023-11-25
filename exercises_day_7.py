""" Exercises Teclado https://teclado.com/30-days-of-python/python-30-day-7-split-join/ """

# Exercise 1
name, surname = input("Enter your name and your surname:    ").strip().split(" ")

# Exercise 2
liste = [1, 2, 3, 4, 5]

processed_numbers = []

for element in liste:
    processed_numbers.append(str(element))

print("|".join(processed_numbers))

# Exercise 3
quotes = [
    "'What a waste my life would be without all the beautiful mistakes I've made.'",
    "'A bend in the road is not the end of the road... Unless you fail to make the turn.'",
    "'The very essence of romance is uncertainty.'",
    "'We are not here to do what has already been done.'"
]

for quote in quotes:
    print(f"{quote[1:-1]}")

# Exercise 4
word = input("Enter a word: ").strip()

print(len(word))
