
def f():
    x = 20

    def g():
        x = 40

        def h():
            nonlocal x 
            x = 60
            print(x)
        h()
        print(x)
    g()
    print(x)

f()

# print(x) # Error: x is not defined