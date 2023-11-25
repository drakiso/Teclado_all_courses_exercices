""" Exercises Teclado https://teclado.com/30-days-of-python/python-30-day-17-args-kwargs/"""

# Exercise 1
def number_sum(*args):
    return sum(args)


# Exercise 2
def arg_printer(*args, **kwargs):
    print(f"Positional arguments are: {args}")
    print(f"Keyword arguments are: {kwargs}")

# Exercise 3
country = {
    "name": "Germany",
    "population": "83 million",
    "capital": "Berlin",
    "currency": "Euro"
}

country_template = """Name: {name}
Population: {population}
Capital: {capital}
Currency: {currency}"""

print(country_template.format(**country))

# Exercise 4
print(*range(1, 21), sep=",")

# Exercise 5
print(*range(1, 21), sep="\n")
