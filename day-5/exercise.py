#exercise-1
movies = ["Interstellar", "3 Idiots", "Inception"]

for movie in movies:
    print(movie)

#exercise-2
student = {
    "name": "Ashutosh",
    "course": "Data Analytics",
    "semester": 6
}

for key, value in student.items():
    print(key, ":", value)

#exercise-3
numbers = [10,20,30,10,20,40]

unique_numbers = set(numbers)

print(unique_numbers)

#exercise-4
cart = []

cart.append("Laptop")
cart.append("Mouse")
cart.append("Keyboard")

print(cart)