#exercise-1
number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")

#exercise-2
num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))

if num1 > num2:
    print("Largest Number:", num1)
else:
    print("Largest Number:", num2)

#exercise-3
marks = int(input("Enter Marks: "))

if marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")
elif marks >= 60:
    print("Grade D")
else:
    print("Fail")
#exercise-4
password = input("Enter Password: ")

if password == "python123":
    print("Access Granted")
else:
    print("Access Denied")
#mini-project– Employee Bonus Calculator
employee_name = input("Employee Name: ")
salary = float(input("Monthly Salary: "))

if salary >= 50000:
    bonus = salary * 0.20
elif salary >= 30000:
    bonus = salary * 0.10
else:
    bonus = salary * 0.05

print("\n------ BONUS REPORT ------")
print(f"Employee : {employee_name}")
print(f"Salary   : ₹{salary:,.2f}")
print(f"Bonus    : ₹{bonus:,.2f}")
