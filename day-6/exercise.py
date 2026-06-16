#exercise-1
def square(number):
    return number * number

num = int(input("Enter Number: "))
print("Square =", square(num))

#exercise-2
def check_even(number):

    if number % 2 == 0:
        return "Even"

    return "Odd"

num = int(input("Enter Number: "))

print(check_even(num))

#exercise-3
def welcome_student(name):
    print(f"Welcome, {name}!")

student = input("Enter Student Name: ")

welcome_student(student)

#exercise-4
def rectangle_area(length, width):
    return length * width

length = float(input("Length: "))
width = float(input("Width: "))

print("Area =", rectangle_area(length, width))