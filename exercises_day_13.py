""" Exercises Teclado https://teclado.com/30-days-of-python/python-30-day-13-return-statements/"""

# Exercise 1
def exponentiate(base, power):
    return base ** power

# Exercise 2
def process_string(string):
    return string.lower().strip()

# Exercise 3
def movie_data(movie_info):
    movie_info_dic = dict()

    movie_info_dic["name"] = movie_info[0]
    movie_info_dic["nationality"] = movie_info[1]
    movie_info_dic["age"] = movie_info[2]

    return movie_info_dic

# Exercise 4
def prime_number(number):
    if number < 2:
        return False

    for divisor in range(2, number):
        if number % divisor == 0:
            return False

    return True
