class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart
        print("init done.")
    
    def f(self):
        print("f Done.")


x = Complex(3.0, -4.5)
print(x)
print(x.r)
print(x.i)

    
xf = x.f
while True:
    print(xf())
