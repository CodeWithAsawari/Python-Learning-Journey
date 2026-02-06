# Set
#Sets are used to store multiple items in a single variable.
# Set items are unchangeable, but you can remove items and add new items

a={"Asawari","Sanjay","Shraddha"}
print(a)
#Set items are unordered, unchangeable, and do not allow duplicate values.

#Duplicates Not Allowed
a={"Asawari","Sanjay","Sanjay"}
print(a)

#The values True and 1 are considered the same value in sets, and are treated as duplicates:
a={"Asawari","Sanjay",1,True}
print(a)

#False and 0 is considered the same value:
a={"Asawari","Sanjay",0,False}
print(a)

#Get the Length of a Set
a={"Asawari","Sanjay","Sanjay"}
print(len(a))

#Set Items - Data Types
a={"Asawari","Sanjay","Sanjay"}
b={1,2,3}
c={True,False,True}

a={"Asawari","Sanjay","Sanjay"}
print(type(a))

#The set() Constructor
a=set(("Asawari","Sanjay"))
print(a)

#Access Items
#You cannot access items in a set by referring to an index or a key.
