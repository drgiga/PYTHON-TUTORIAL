def myFunction():
    print("myFunction is Done.")

def summation(num1,num2):
    num1+num2

def multiply(num1,num2):
    return num1+num2

def printResult(num1,num2):
    return print(num1+num2)
print("-----------------------------")
myFunction()
print(summation(5,6))
print(multiply(4,3))
printResult(7,8)
print("-----------------------------")
def function1(fn = "default name" , ln = "last name"):
    return print(fn,ln)

function1()
function1("davoud")
function1(None,None)
function1(None,"keramati")
print("-----------------------------")
def compareFunction(first_input = None,last_input = None):
    if ((first_input is None) or (last_input is None)):
        return print(None) # Or --> return None Or --> return
    elif (first_input > last_input):
        return print("first in greater than last")
    elif (first_input < last_input):
        return print("first is less than last")
    else:
        return print("first and last are equal.")

compareFunction(10,10)

