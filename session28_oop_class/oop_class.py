from tkinter import N


class Person():
    name = "default_name"
    family = "default_family"
    age = None

    def setName(self,_name):
        self.name = _name
    def getName(self):
        return self.name


print("------------------------")
object1 = Person()
print(dir(object1))

print(Person())
print(Person().getName())
Person().setName("alireza")
print(Person().getName())
print(id(Person))
print(id(Person()))



object1.setName("Farid")
print(object1.getName())
print(id(object1))
