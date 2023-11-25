""" Exercises Teclado https://teclado.com/30-days-of-python/python-30-day-18-imports/"""
import random


# exercise 1
def prime_numbers_generator():
    for number in range(2, 101):
        for divisor in range(2, number):
            if number % divisor == 0:
                break
        else:
            yield number


# exercise 2
names = [" rick", " MORTY  ", "beth ", "Summer", "jerRy    "]
names = (lambda name: name.strip().title() for name in names)

# exercise 3
suits = ['spades', 'hearts', 'diamonds', 'clubs']
ranks = ['ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'jack', 'queen', 'king']

# composition of the deck
deck = [(rank, suit) for suit in suits for rank in ranks]  # I could've use product() of itertools
random.shuffle(deck)
deck = iter(deck)

# ask the number of player
while True:
    number_of_players = input("How many players are there ? ").strip()

    try:
        number_of_players = int(number_of_players)
    except ValueError:
        print("You must enter an integer.")
    else:
        if number_of_players > 10 or number_of_players < 2:
            print("There must be at least 2 players, and no more than 10.")
        else:
            break

# hand card to each player
first_hands = [next(deck) for _ in range(number_of_players)]
second_hands = [next(deck) for _ in range(number_of_players)]

i = 0
for player in range(1, number_of_players+1):
    print(f"Player {player} was dealt: {first_hands[i]}, {second_hands[i]}")
    i += 1

next(deck)
print(f"The flop: {next(deck)}, {next(deck)}, {next(deck)}")
next(deck)
print(f"The turn: {next(deck)}")
next(deck)
print(f"The river: {next(deck)}")
