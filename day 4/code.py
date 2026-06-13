# Day 4 - Loops

# For Loop

for i in range(1, 6):
    print(i)

print("\n")

# Printing Names

for i in range(3):
    print("Ashutosh")

print("\n")

# While Loop

count = 1

while count <= 5:
    print(count)
    count += 1

print("\n")

# Multiplication Table

num = int(input("Enter a Number: "))

for i in range(1, 11):
    print(f"{num} x {i} = {num*i}")