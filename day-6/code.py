# Day 6 - Functions

# Basic Function

def greet():
    print("Welcome to Python Programming!")

greet()

# Function with Parameters

def greet_user(name):
    print(f"Hello, {name}")

greet_user("Ashutosh")

# Function with Return Value

def add(a, b):
    return a + b

result = add(10, 20)

print("Sum =", result)

# Multiple Parameters

def student_info(name, course):
    print(f"Name: {name}")
    print(f"Course: {course}")

student_info("Ashutosh", "Data Analytics")