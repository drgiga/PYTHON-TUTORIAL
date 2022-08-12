class Person:
    name = "Default Name"
    family = "Default Family"
    
    """def __init__(self) -> None:
        pass"""

    def __init__(self, className = "Person"):
        print(f"__init__ Method -> Class:{className} Done.")
        self._className = className
        

    # getter method
    def getClassName(self):
        return self._className
    # setter method
    def setClassName(self, className):
        self._className = className

    def setName(self,name):
        self.name = name
    def getName(self):
        return self.name

    def setFamily(self,family):
        self.family = family
    def getFamily(self):
        return self.family

personObject = Person()

className = personObject.getClassName()
personName = personObject.getName()
personFamily = personObject.getFamily()
print(className)
print(personName)
print(personFamily)

personObject.setClassName("Class Person")
personObject.setName("Davoud")
personObject.setFamily("Keramati")
className = personObject.getClassName()
personName = personObject.getName()
personFamily = personObject.getFamily()
print(className)
print(personName)
print(personFamily)

personObject.__setattr__("age","0")
print(personObject.age)

personObject.__setattr__("birthDayFunc","20 bahman 1366")
print(personObject.birthDayFunc)

def birthDay(input):
    return input

personObject.birthDayFunc = birthDay("22 bahman 1366")
print(personObject.birthDayFunc)


"""personObject = birthDay("23 bahman 1366")
print(personObject)"""
