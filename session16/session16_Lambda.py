# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.

# Syntax
# lambda arguments : expression
# The expression is executed and the result is returned:
print("------------------------------------")
# Add 10 to argument a, and return the result:
x = lambda a : a + 10
print(x(5))
print("------------------------------------")
# Input Davoud and Keramati to arguments name and family, and return the result:
myStr = lambda name , family : "Hello "+name+" "+family
print(myStr("Davoud","Keramati"))
print("------------------------------------")
# Multiply argument a with argument b and return the result:
x = lambda a, b : a * b
print(x(5, 6))
print("------------------------------------")
# Summarize argument a, b, and c and return the result:
x = lambda a, b, c : a + b + c
print(x(5, 6, 2))
print("------------------------------------")
"""
# Why Use Lambda Functions?
The power of lambda is better shown when you use them as an anonymous function inside another function.

# Say you have a function definition that takes one argument, 
# and that argument will be multiplied with an unknown number:
# """

def myfunc(n):
  return lambda a : a * n
# Use that function definition to make a function that always doubles the number you send in:

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(myfunc(2)) # <function myfunc.<locals>.<lambda> at 0x000001DDC9E5A560>
print(mydoubler(11))
print("------------------------------------")
# Or, use the same function definition to make a function that always triples the number you send in:

def myfunc(n):
  return lambda a : a * n

mytripler = myfunc(3)

print(mytripler(11))
print("------------------------------------")
# Or, use the same function definition to make both functions, in the same program:

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))
# Use lambda functions when an anonymous function is required for a short period of time.
print("------------------------------------")