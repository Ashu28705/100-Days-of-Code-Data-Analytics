# Day 3 - Operators & Conditional Statements

# Arithmetic Operators

a = 20
b = 5

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)

# Comparison Operators

x = 10
y = 20

print(x == y)
print(x != y)
print(x > y)
print(x < y)

# Logical Operators

age = 21
has_id = True

print(age >= 18 and has_id)
print(age >= 18 or has_id)
print(not has_id)

# Conditional Statements

age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")