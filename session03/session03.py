x0 = 4       # x is of type int
x0 = "Sally" # x is now of type str
print(x0)

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

print(x)
print(y)
print(z)
#------------------------------------------------
# Naming Variables in Python

# Legal Naming variables in python:
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

# Illegal Naming variables in python:

# 2myvar = "John"
# my-var = "John"
# my var = "John"
#------------------------------------------------
# Assign Multiple Values
x2, y2, z2 = "Orange", "Banana", "Cherry"
print(x2)
print(y2)
print(z2)
# Assign One Value to Multiple Variables
x3 = y3 = z3 = "Orange"
print(x3)
print(y3)
print(z3)
# Unpack a Collection
fruits = ["apple", "banana", "cherry"]
x4, y4, z4 = fruits
print(x4)
print(y4)
print(z4)