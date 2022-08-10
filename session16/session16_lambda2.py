multiply =lambda num:num*num
print(lambda num:num*num)
print(multiply)
print(multiply.__name__)
print(multiply(5))
print("*******************************")
sum = lambda first,second :first+second
print(sum)
print(sum.__name__)
print(sum(4,6))
print("*******************************")
minus = lambda first,second :first-second

def myFunc(input):
    print(input)

myFunc(minus(10,6))

summation = lambda first,second :first+second

def myFunc(input):
    print(input)

myFunc(summation(10,6))

division = lambda first,second :first/second

def myFunc(input):
    print(input)

myFunc(division(300,6))

print(minus.__name__)
print(summation.__name__)
print(division.__name__)

print(myFunc.__name__)