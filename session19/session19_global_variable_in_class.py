class AAA:
    def aaa1(self):
        global localvar
        localvar = "local variable"
        global globalvar
        globalvar = "global variable"
        print(globalvar)

print("----------------------------------")
obj1 = AAA().aaa1
print(obj1)
print("----------------------------------")
obj2 = AAA().aaa1()
print(obj2)

class BBB:
    def __init__(self):  # default constructor
        print("__init__ method done.")

    """def __init__(self,name = "Default Name",family = "Default Family"): 
        self.name = name
        self.family = family
        print(self.name,self.family)"""
        

    def bbb1(self):
        print("----------------------------------")
        print("in class BBB: "+globalvar)

    def bbb2(input1,input2):
        print("----------------------------------")
        print("in class BBB: "+globalvar+","+input2)

class CCC:
    def ccc1(self):
        print("----------------------------------")
        print("in class CCC: "+globalvar)   

BBB()
# BBB("ali","rahmati")
BBB.bbb1(globalvar)
BBB.bbb2(globalvar,localvar)

CCC.ccc1(globalvar)