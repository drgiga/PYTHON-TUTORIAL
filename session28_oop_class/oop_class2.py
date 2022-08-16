from tkinter import N


class Person():
    name = "default_name"
    family = "default_family"
    age = None

    def __init__(self,_name,_family,_age):
        self.name = _name
        self.family = _family
        self.age = _age
        return None

    def setName(self,_name):
        self.name = _name
    def getName(self):
        return self.name


print("------------------------")
object1 = Person("shahrooz","tabatabaei",65)
print(dir(object1))

print(Person("ali","kalimi",40))
print(Person("ali","kalimi",40).getName())
Person("ali","kalimi",40).setName("alireza")
print(Person("ali","kalimi",40).getName())
print(id(Person))
print(id(Person("ali","kalimi",40)))


Person("ali","kalimi",40).__init__("Mohammad","Ghasemi",55)
object1.setName("Farid")
print(object1.getName())
print(id(object1))

print(Person("mohadeseh","keramati",25).getName())