# Arithmetic Operators
a = 4
b = 5
print(a+b)  # addition
print(a-b)  # subtraction
print(a*b)  # Multiplication
print(a/b)  # division
print(a//b) # floor division
print(a%b)  # Modulus
print(a**b) # Exponentiation

# Assignment Operators
a = 5  # = operator
print(a)
a=3
a += 5  # += operator
print(a)
a-=5  # -= operator
print(a)
a*=5 # *= operator
print(a)
x = 5
x /= 3 # /= operator
print(x)
x = 5
x%=3 # %= operator
print(x)
x = 5
x//=3 # //= operator
print(x)
x = 5
x **= 3 # **= operator
print(x)
x = 5
x &= 3 # &= operator
print(x)
x = 5
x |= 3 # |= operator
print(x)
x = 5
x ^= 3  # ^= operator
print(x)
x = 5
x >>= 3 # >>= operator
print(x)
x = 5
x <<= 3 # <<= operator
print(x)
print(x := 3) # := operator

# Comparison Operators
x = 5
y = 3
print(x == y) # returns False because 5 is not equal to 3
x = 5
y = 3
print(x != y) # returns True because 5 is not equal to 3
x = 5
y = 3
print(x > y) # returns True because 5 is greater than 3
print(x < y) # returns false because 5 is greater than 3
print(x >= y)
print(x <= y)

# Logical Operators
x = 5
print(x > 3 and x < 10) # returns True because 5 is greater than 3 AND 5 is less than 10
x = 5
print(x > 3 or x < 4)
# returns True because one of the conditions are true (5 is greater than 3, but 5 is not less than 4)
x = 5
print(not(x > 3 and x < 10))
# returns False because not is used to reverse the result

# Identity Operators

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z)
# returns True because z is the same object as x
print(x is y)
# returns False because x is not the same object as y, even if they have the same content
print(x == y)
# to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y

# Membership Operators

x = ["apple", "banana"]

print("banana" in x)
# returns True because a sequence with the value "banana" is in the list
x = ["apple", "banana"]

print("pineapple" not in x) # returns True because a sequence with the value "pineapple" is not in the list

# Bitwise Operator
print(6 & 3)  #The & operator compares each bit and set it to 1 if both are 1, otherwise it is set to 0:
#6 = 0000000000000110
#3 = 0000000000000011
#--------------------
#2 = 0000000000000010
print(6 | 3)
""" The | operator compares each bit and set it to 1 if one or both is 1, otherwise it is set to 0:

6 = 0000000000000110
3 = 0000000000000011
--------------------
7 = 0000000000000111 """
# The ^ operator compares each bit and set it to 1 if only one is 1, otherwise it is set to 0
# 6 = 0110
# 3 = 0011
# --------
# 5 = 0101

print(6 ^ 3)
print(~3)
"""
The ~ operator inverts each bit (0 becomes 1 and 1 becomes 0).

Inverted 3 becomes -4:
 3 = 0000000000000011
-4 = 1111111111111100 """

print(3 << 2)



"""
The << operator inserts the specified number of 0's (in this case 2) from the right and let the same amount of leftmost bits fall off:

If you push 00 in from the left:
 3 = 0000000000000011
becomes
12 = 0000000000001100"""
print(8 >> 2)

"""
The >> operator moves each bit the specified number of times to the right. Empty holes at the left are filled with 0's.

If you move each bit 2 times to the right, 8 becomes 2:
 8 = 0000000000001000
becomes
 2 = 0000000000000010"""