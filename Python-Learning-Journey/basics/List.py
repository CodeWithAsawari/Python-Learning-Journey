#Create a List:
a = ["Asawari","Sanjay"]
print(a)
# List items are ordered, changeable, and allow duplicate values.

# List Length
#To determine how many items a list has, use the len() function:
a = ["Asawari","Sanjay" ]
print(len(a))

#The list() Constructor
#It is also possible to use the list() constructor when creating a new list.
a = list(("Asawari","Sanjay" ))
print(a)

#Access list items
a = ["Asawari","Sanjay" ]
print(a[1])
print(a[-1])
print(a[0:1])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
#The search will start at index 2 (included) and end at index 5 (not included).

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])
#This will return the items from index 0 to index 4.

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])
#This will return the items from index 2 to the end.

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])
#This example returns the items from index -4 (included) to index -1 (excluded)
#Remember that the last item has the index -1

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist) #Change the second and third value by replacing it with one value:

# Insert list items
a = ["Asawari","Sanjay" ]
a.insert(0,"Sanjay") # .insert() is used
print(a)

a = ["Asawari","Sanjay" ]
a.append("Sanjay") # .append() is used
print(a)

a = ["Asawari","Sanjay" ]
b= ["Asawari","Sanjay" ]
a.extend(b)
print(a)

# The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).

# Remove list items
a = ["Asawari","Sanjay","Shraddha" ]
a.remove("Shraddha")  # remove() is used
print(a)

a = ["Asawari","Sanjay","Shraddha" ]
a.pop(2) # pop() is used
print(a)

a = ["Asawari","Sanjay","Shraddha" ]
del a[2] # del is used
print(a)

a = ["Asawari","Sanjay","Shraddha" ]
a.clear()
print(a)
