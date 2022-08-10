class AAA:
    def aaa1(self):
        localvar = "local variable"
        print(localvar)

print("----------------------------------")
obj1 = AAA().aaa1
print(obj1)
print("----------------------------------")
obj2 = AAA().aaa1()
print(obj2)