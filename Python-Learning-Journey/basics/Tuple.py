# Tuple
#A tuple is a collection which is ordered and unchangeable.
#Tuple items are ordered, unchangeable, and allow duplicate values.
a = ("Asawari","Sanjay")
print(a)

#Allow Duplicates
a = ("Asawari","Sanjay","Sanjay")
print(a)

#Tuple Length
a = ("Asawari","Sanjay","Sanjay")
print(len(a))

#Create Tuple With One Item

a= (" asawari",)
print(type(a))

#NOT a tuple
a = ("asawari")
print(type(a))

#Tuple Items - Data Types
a=("Asawari","Sanjay",)
b=(1,2,3)
c=(True,False)
print(a,b,c)

#The tuple() Constructor
a=tuple(("asawari","Sanjay"))
print(a)

#Access Tuple Items
a=("Asawari","Sanjay")
print(a[1])

#Range of Indexes
a=("Asawari","Sanjay","Shraddha","Prajkta","Samruddhi","Aditi")
print(a[2:5])

a=("Asawari","Sanjay","Shraddha","Prajkta","Samruddhi","Aditi")
print(a[:4]) #By leaving out the start value, the range will start at the first item:

a=("Asawari","Sanjay","Shraddha","Prajkta","Samruddhi","Aditi")
print(a[2:]) #By leaving out the end value, the range will go on to the end of the tuple:

a=("Asawari","Sanjay","Shraddha","Prajkta","Samruddhi","Aditi")
print(a[-4:-1]) #Specify negative indexes if you want to start the search from the end of the tuple

#Change Tuple Values
a=("Asawari","Shradha")
b=list(a)
b[1]="Sanjay"
a=tuple(b)
print(a)

#Add Items
# 1) Convert into a list:
a=("Asawari","Shradha")
b=list(a)
b.append("Sanjay")
a=tuple(b)
print(a)

#Add tuple to a tuple
a=("Asawari","Shradha")
b=("Sanjay",)
a+=b
print(a)

 #Remove Items
 #Tuples are unchangeable,Convert the tuple into a list, remove "apple", and convert it back into a tuple:
a=("Asawari","Shradha")
b=list(a)
b.remove("Shradha")
a=tuple(b)
print(a)

#The del keyword can delete the tuple completely:
"""a=("Asawari","Shradha")
del a
print(a) """##this will raise an error because the tuple no longer exists

#Unpacking a Tuple
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

#Using Asterisk*

#If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

#If the asterisk is added to another variable name than the last, Python will assign values to the variable until the number of values left matches the number of variables left.
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)
