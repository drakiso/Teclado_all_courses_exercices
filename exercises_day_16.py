""" Exercises Teclado https://teclado.com/30-days-of-python/python-30-day-16-exercise-solutions/"""

# Exercise 1
students = [
    {"name": "Hannah", "grade_average": 83},
    {"name": "Charlie", "grade_average": 91},
    {"name": "Peter", "grade_average": 85},
    {"name": "Rachel", "grade_average": 79},
    {"name": "Lauren", "grade_average": 92}
]

students.sort(key=lambda student: student["name"])

print(students)

# Exercise 2
exp = lambda base, exponent: base ** exponent

# Exercise 3
print(exp)
