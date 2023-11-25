""" Exercises Teclado https://teclado.com/30-days-of-python/python-30-day-5-conditionals-booleans/ """

# Exercise 1
numbers = [1, 2, 3, 4]
new_numbers = numbers + [5]
numbers.append(5)

print(numbers is new_numbers)

# Exercise 2
number = int(input("Enter a number: "))

if number > 0:
    print(f"{number} is positive")
elif number < 0:
    print(f"{number} is negative")
else:
    print("You entered 0")

# Exercise 3
worked_hours = int(input("Enter the number of hours the employee worked this week:  "))
hourly_wage = int(input("Enter the employee's hourly wage:  "))

if worked_hours <= 40:
    print(f"Employee's pay is ${worked_hours * hourly_wage:.2f}")
else:
    print(f"Employee's pay is $"
          f"{(worked_hours - 40) * hourly_wage * 1.1 + worked_hours * hourly_wage:.2f}")
