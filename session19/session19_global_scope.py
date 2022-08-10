x = 300 # global

def myfunc():
    x = 200 # local
    print(x)

myfunc()

print(x)
print("---------------------------------------")
y = 'global'
def f():
    
    def g(input):
        print(input)
    
    g(y) # call in f()

    print(y)
f()
print("---------------------------------------")