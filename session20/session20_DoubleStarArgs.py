def printAllArguments(*args):
    return args

result = printAllArguments("davoud","keramati",25,451000,True,False,None)

print(type(result)) # <class 'tuple'>
print(result)
print("------------------------------")
def printSumOfAllArguments(*args):
    print(type(args)) # <class 'tuple'>
    totalSum = 0
    for number in args:
        totalSum = number + totalSum
    return totalSum

result = printSumOfAllArguments(1,2,3,4,5,6,7,8,9,0)
print(type(result)) # <class 'int'>
print(result)
print("-----------------------------")
result = printSumOfAllArguments(1.11,22.54,39.654,44128.21,98.55,100.66,45.7,987520.008,9.0,0.0)
print(type(result)) # <class 'int'>
print(result)
print("-----------------------------")
result = printSumOfAllArguments(1+6j,-22.54-3j,1+4j,-8+8j)
print(type(result)) # <class 'int'>
print(result)
print("*******************************")
def print2AndMore(name,family,*args):
    print(type(name)) # <class 'tuple'>
    print(type(family)) # <class 'tuple'>
    print(type(args)) # <class 'tuple'>

    totalSum = 0
    for elm in args:
        if(type(elm) == int):
            totalSum = elm + totalSum
        elif(type(elm) == str):
            name,family = elm , elm
            # return elm
    return print(name , family , totalSum)
    # return print(name , family , totalSum , type(name),type(family) , type(totalSum))
    
result = print2AndMore("davoud","keramati",1,2,3,4,5,6,7,8,9)
print(type(result)) # <class 'int'>
print(result)
print("*******************************")
def showInfo(**args):
    return print(args) # return a dictionary of {key and value}

showInfo(name="davoud",family="keramati",age=35)
print("*******************************")
def showInfo(**kwargs):
    return print(kwargs) # return a dictionary of {key and value}

showInfo(name="davoud",family="keramati",age=35)
print("*******************************")
def showInfo(*args,**kwargs):
    return print(kwargs) # return a dictionary of {key and value}

showInfo(name="davoud",family="keramati",age=35)
showInfo(name="davoud",family="keramati",age=35,height=187.5)
showInfo(name="davoud",family="keramati",age=35,height=187.5,weight=82.5)
showInfo(name="davoud",family="keramati")
showInfo(name="davoud")
print("*******************************")
def showInfo2(*args,**kwargs):
    for key,value in kwargs.items():
        print("key is:",key ,"value is:", value)
        print(f"{key}:{value}")
    print("---------------")
    return print(kwargs) # return a dictionary of {key and value}

showInfo2(name="davoud",family="keramati",age=35,height=187.5,weight=82.5)
print("*******************************")
# Order of use:
#   Parameters
#   *args
#   Default Parameters
#   **kwargs

def displayInfo(name,family,age,*args,defaultCity = "Chicago" , defaultCountry = "USA",**kwargs):
    return print([name,family,age,args,defaultCity,defaultCountry,kwargs])

displayInfo("Davoud","Keramati",35,55,75,"python",[1,2,3],{"key1":"value1","key2":"value2"},1000,defaultCity="Arak",defaultCountry="IRAN",course="programming",score=100)
print("*******************************")
def sum_all_numbers(*args):
    print("args = ",args)
    totalSum = 0
    for item in args:
        totalSum += item
    return totalSum

numbers = [1,2,3,45,98,102,14785]
sum_all_numbers(*numbers)
# sum_all_numbers(numbers) # TypeError: unsupported operand type(s) for +=: 'int' and 'list'
print("*******************************")
def display_names(name,family):
    print(f"name is: {name} , family is: {family}")

display_names("Davoud" , "Keramati")
print("*******************************")
person_object = {
    "name":"Davoud",
    "family":"Keramati"
}
display_names(**person_object)