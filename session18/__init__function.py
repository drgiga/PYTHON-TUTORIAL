class MyClass:
    def __init__(self):
        print("init done.")


MyClass() 

# When a class defines an __init__() method, 
# class instantiation automatically invokes __init__() for the newly created class instance

print("---------------------------------------")
class AAA:
    def __init__(self):
        self.data = []
        print(self.data)
        print(self)
        print("__init__ done.")


AAA()
# AAA().__init__()


class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

x = Complex(3.0, -4.5)
x.r, x.i

print(x)
print(x.r)
print(x.i)