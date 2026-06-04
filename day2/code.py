# Day 2 - Strings and Type Casting

name = "Ashutosh"

print(name)
print(type(name))

# String Indexing

print(name[0])
print(name[1])
print(name[-1])

# String Slicing

print(name[0:4])
print(name[2:6])

# String Methods

message = "python programming"

print(message.upper())
print(message.lower())
print(message.title())
print(message.capitalize())

# Length

print(len(message))

# Replace

print(message.replace("python", "Java"))

# Type Casting

age = "21"

print(type(age))

age = int(age)

print(type(age))

# f-Strings

name = "Ashutosh"
course = "Data Analytics"

print(f"My name is {name} and I am learning {course}")