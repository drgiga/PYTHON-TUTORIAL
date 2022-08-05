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
my_var = "John" # Snake Case Naming
_my_var = "John"
myVar = "John" # Camel Case Naming
MyVar = "John" # Upper Camel Case Naming
MYVAR = "John" # Upper Case Naming
myvar2 = "John" # Lower Case Naming
__my_var__  = "John"
__MY_VAR__  = "John"
PI = 3.14

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
#------------------------------------------------
# Output Variables
xstring = "Python is awesome"
print(xstring)
print(xstring,type(xstring))
print('------------------------------')
xstr = "Python"
ystr = "is"
zstr = "awesome"
print(xstr, ystr, zstr)
print('------------------------------')
xstr2 = "Python "
ystr2 = "is "
zstr3 = "awesome"
print(xstr2 + ystr2 + zstr3)
print('------------------------------')
xvar = 5
yvar = 10
print(xvar+yvar)
print(xvar , type(xvar) ,  yvar , type(yvar))
print('------------------------------')
xvar2 = 5
yvar2 = "John"
#print(xvar2+yvar2) # error TypeError: unsupported operand type(s) for +: 'int' and 'str'
print(xvar2,type(xstring) , yvar2,type(yvar2))
print('------------------------------')
xvar3 = 5
yvar3 = "John"
print(xvar3,yvar3)
print(xvar3,type(xvar3), yvar3,type(yvar3))