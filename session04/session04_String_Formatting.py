#1 “Old Style” String Formatting (% Operator)
name = 'davoud'
'Hello, %s' % name
print('Hello, %s' % name)
print("-----------------------------------")
#2 “New Style” String Formatting (str.format)
firstname = "ali"
'Hello, {}'.format(firstname)
print('Hello, {}'.format(firstname))
print("-----------------------------------")
#3 String Interpolation / f-Strings (Python 3.6+)
f'Hello, {name}!'
print(f'Hello, {name}!')
#-----------------------------------------
# sample for numbers
a = 5
b = 10
f'Five plus ten is {a + b} and not {2 * (a + b)}'
print(f'Five plus ten is {a + b} and not {2 * (a + b)}')
#-----------------------------------------
# sample in a function
def greet(name, question):
    return f"Hello, {name}! How's it {question}?"

print(greet('Bob', 'going'))
#-----------------------------------------
#sample for show errors
errorno = 50159747054
f"Hey {name}, there's a {errorno:#x} error!"
print(f"Hey {name}, there's a {errorno:#x} error!")
