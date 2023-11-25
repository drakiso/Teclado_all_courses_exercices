""" Exercises Teclado https://teclado.com/30-days-of-python/python-30-day-6-for-loops/ """

# Exercise 1
employees = [
    ("Rolf Smith", 35, 8.75),
    ("Anne Pun", 30, 12.50),
    ("Charlie Lee", 50, 15.50),
    ("Bob Smith", 20, 7.00)
]

for employee in employees:
    print(f"{employee[0]} is due to be paid {employee[1] * employee[2]}")

# Exercise 2
sum_hourly_wage = 0

for employee in employees:
    sum_hourly_wage += employee[2]

average_wage = sum_hourly_wage / len(employees)

for employee in employees:
    if employee[2] > average_wage:
        print(f"{employee[0]}'s hourly is above average")
