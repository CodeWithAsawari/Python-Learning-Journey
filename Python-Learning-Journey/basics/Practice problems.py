#smart login system
#conditions of python concept used
correct_username = "admin"
correct_password = "1234"

username = input("Enter username: ")
password = input("Enter password: ")

if username == correct_username and password == correct_password:
    print("Login Successful ")
else:
    print("Invalid Credentials")
    
# Student Result Management System 

name= input("Enter student name:")
roll_no=int(input("Enter roll no:"))

subject1=int(input("Enter subject 1 marks:"))
subject2=int(input("Enter subject 2 marks:"))
subject3=int(input("Enter subject 3 marks:"))
subject4=int(input("Enter subject 4 marks:"))

total=subject1+subject2+subject3+subject4
percentage=total/4
if percentage>=75:
    grade="A"
elif percentage>=60:
    grade="B"
elif percentage>=40:
    grade="C"
else:
    grade="Fail"

print("STUDENT RESULT")
print(f"Name        : {name}")
print(f"Roll No     : {roll_no}")
print(f"Total Marks : {total}")
print(f"Percentage  : {percentage}%")
print(f"Grade       : {grade}")

# Simple Calculator
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("1.Add  2.Subtract  3.Multiply  4.Divide")
choice = int(input("Choose operation: "))

if choice == 1:
    print("Result:", a + b)
elif choice == 2:
    print("Result:", a - b)
elif choice == 3:
    print("Result:", a * b)
elif choice == 4:
    if b != 0:
        print("Result:", a / b)
    else:
        print("Cannot divide by zero")
else:
    print("Invalid choice")
