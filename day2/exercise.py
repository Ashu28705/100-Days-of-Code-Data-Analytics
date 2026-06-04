#Ex-1 Personal profile generator
name = input("Enter your name: ")
age = int(input("Enter your age: "))
city = input("Enter your city: ")

print("\n----- PROFILE -----")
print(f"Name : {name}")
print(f"Age  : {age}")
print(f"City : {city}")

#Ex-2 Username generator
first_name = input("First Name: ")
last_name = input("Last Name: ")

username = first_name.lower() + "_" + last_name.lower()

print("Suggested Username:", username)

#Ex-3 Email analyzer
email = input("Enter Email: ")

print("Length:", len(email))
print("Upper:", email.upper())
print("Lower:", email.lower())

#Ex-4 Word counter
sentence = input("Enter a sentence: ")

words = sentence.split()

print("Number of words:", len(words))