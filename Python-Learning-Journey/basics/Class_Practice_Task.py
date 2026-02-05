#Task 1
#in this task we have assigned variables and end,sep is used
Student_name = "Asawari"
Student_rollNo = 41
Student_adhaarNo = 123456
Student_dept =  "AIDS"
print("My name is", Student_name,end=" ", sep=" ")
print("from",Student_dept,"department",end=" ", sep=" ")
print("having roll no",Student_rollNo,end=" ", sep=" ")
print("and having addhar no",Student_adhaarNo,end=" ", sep=" ")

#Task 2
# in this task f-string concept is used
Student_name = input("Enter your name: ") #this take input name from the user
Student_rollNo = int(input("Enter roll no: ")) #this take input roll no
Student_adharNo = int(input("Enter aadhar no: ")) #this take input aadhar
Student_dept = input("Enter dept: ") #this take input dept
print(f"My name is {Student_name} from {Student_dept} department having roll no {Student_rollNo} and Aadhar no {Student_adharNo}")

#Task 3
Student_name = input("Enter your name: ")  # this take input name from the user
Student_rollNo = int(input("Enter roll no: "))  # this take input roll no
Student_adharNo = int(input("Enter aadhar no: "))  # this take input aadhar
Student_dept = input("Enter dept: ")  # this take input dept

Marks_oF_OS = int(input("Enter OS marks: "))  # this takes input marks of 4 subjects
Marks_oF_PYTHON = int(input("Enter Python marks: "))
Marks_oF_DATA_ANALYSIS = int(input("Enter Data Analysis marks: "))
Marks_oF_DM = int(input("Enter DM marks: "))

print(f"My name is {Student_name} from {Student_dept} department having roll no {Student_rollNo} and Aadhar no {Student_adharNo}. Marks are: OS={Marks_oF_OS}, Python={Marks_oF_PYTHON}, Data Analysis={Marks_oF_DATA_ANALYSIS}, DM={Marks_oF_DM}.")
# using f string output will printed in 1 single line

#Task 4
Marks = int(input("Enter Marks: "))
print(f"Marks : {Marks}")
if Marks >= 80: # if is used for checking the condition
    print("Grade A")
elif Marks >= 65: # if not satisfied then elif condition will check
    print("Grade B")
elif Marks >= 50:
    print("Grade C")
elif Marks >= 35:
    print("Pass")
else: # at the last condition this will be printed
    print("Fail")
#Task 5
Marks = int (input("Enter Marks: "))
Attendance = int (input("Enter Attendance % : "))
if Marks >=90:
    if Attendance >= 75:
        print("Eligible for full scholarship")
elif Marks >=75:
    if Attendance >= 75:
        print("Eligible for partial scholarship")
elif Marks >=50:
    if Attendance<75:
        print("Not Eligible for scholarship")
else:
    print("Fail")
#Task 6
num = int(input("Enter a number: "))
if num % 3 == 0 and num % 5 == 0:
    print("FizzBuzz")
elif num %3==0:
    print("Fizz")
    if num %5==0:
     print("Buzz")
else:
    print(num)
# Task7
Marks = int(input("Enter Marks: "))
print(f"Marks : {Marks}")
if Marks >= 80: # if is used for checking the condition
    print("Grade A")
elif Marks >= 65: # if not satisfied then elif condition will check
    print("Grade B")
elif Marks >= 50:
    print("Grade C")
elif Marks >= 35:
    print("Pass")
else: # at the last condition this will be printed
    print("Fail")

# Task8
#Task 9
Marks = int (input("Enter Marks: "))
Attendance = int (input("Enter Attendance % : "))
if Marks >=90:
    if Attendance >= 75:
        print("Eligible for full scholarship")
elif Marks >=75:
    if Attendance >= 75:
        print("Eligible for partial scholarship")
elif Marks >=50:
    if Attendance<75:
        print("Not Eligible for scholarship")
else:
    print("Fail")


