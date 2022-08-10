x = 20 # global
def f():
    global x # declared global
    x = 40
    print(x)

f()
print("----------------------------------")
x = 20 # global
def f():
    global x # declared global
    x = 40
    def ff():
        global x # declared global
        x = 60
        print(x)
    ff()
    print(x)
    
f()
print("----------------------------------")
x = 20
def f():
    globals()['x'] = 40
    print(x)
f()
x
print("----------------------------------")
def f():
    x = 20

    def g():
        x = 40

        def h():
            global x 
            x = 60
            print(x)
        h()
        print(x)
    g()
    print(x)

f()

print("global" , x)