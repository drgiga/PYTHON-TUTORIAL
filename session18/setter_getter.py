class MyClass:
    
    def __init__(self, className = "MyClass"):
        self._className = className
    # getter method
    def getClassName(self):
        return self._className
    # setter method
    def setClassName(self, className):
        self._className = className

myObject1 = MyClass()
# setting the age using setter
myObject1.setClassName("new Class")
# retrieving age using getter
print(myObject1.getClassName())
print(myObject1._className)



