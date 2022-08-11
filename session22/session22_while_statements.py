from typing import Tuple


print("##################### while statement in List #####################")
myList = [1,2,3,4,5,6,7,8,9,0]

i = 0   
while i < len(myList):
    print(myList[i])
    i = i + 1
print("---------------------------------")
myList = ["1","2","3","4","5","6","7",'8',"9","0"]

i = 0   
while i < len(myList):
    print(myList[i])
    i = i + 1
print("---------------------------------")
myList = [True,False,None]

i = 0   
while i < len(myList):
    print(myList[i])
    i = i + 1
print("---------------------------------")
myList = [True,False,None,"fsdfsdf","dfgfdgg",'kkkk',1+9j,-1001,500,[0,0,0,0],{1,1,1,1},{1,2,3,4,5,6},{"name":"davoud"},(True,False,'kkkk',1+9j,-1001,500)]

i = 0   
while i < len(myList):
    print(myList[i])
    i = i + 1
print("**************************************************************************************")
myList = [{1,2,3,4,5,6,7,8,9,0}]

length = len(myList)
print("length",length)
print(myList[length-1])
print(type(myList[length-1]))

while (length != 0):
    for i in myList[length-1]:
        print(i)
    length -= 1
print("length",length)
print("**************************************************************************************")
myList = [[1,2,3,4,5,6,7,8,9,0]]

length = len(myList)
print("length",length)
print(myList[length-1])
print(type(myList[length-1]))

while (length != 0):
    for i in myList[length-1]:
        print(i)
    length -= 1
print("length",length)
print("**************************************************************************************")
myList = [(1,2,3,4,5,6,7,8,9,0)]

length = len(myList)
print("length",length)
print(myList[length-1])
print(type(myList[length-1]))

while (length != 0):
    for i in myList[length-1]:
        print(i)
    length -= 1
print("length",length)
print("**************************************************************************************")
myList = [{"item1":"1","item2":"2","item3":"3","item4":"4"}]

length = len(myList)
print("length",length)
print(myList[length-1])
print(type(myList[length-1]))

while (length != 0):
    for i in myList[length-1]:
        print(i , myList[length-1][i])
    length -= 1
print("length",length)
print("##################### while statement in Set #####################")
mySet = {1,2,3,4,5,6,7,8,9,0}

i = 0
x = 0

flag = 0
while (flag == 0):
    output = lambda : [print(x) for x in mySet]
    print(output())
    flag = 1
print("**************************************************************************************")
mySet = {"ali","hadi","dfgfdgg",'kkkk',1+9j,-1001,500}
x = 1
length = len(mySet)
while (length > x):
    #print(mySet)
    output = lambda : [print(x) for x in mySet]
    print(output())
    length = length - 1
print("**************************************************************************************")
mySet = {"ali","hadi""dfgfdgg",'kkkk',1+9j,-1001,500}

i = 0
x = 0
length = len(mySet)
flag = 0
while (flag == 0):
    output = lambda : [print(x) for x in mySet]
    print(output())
    flag = 1
print("**************************************************************************************")
print("Fetching (Set Items) in a List")
data = [{1,2,3,4,5,6,7,8,9,0}]
print("Before Convert:",data , type(data))
data = tuple(data)
print("After Convert:",data , type(data))

length = len(data)
print("length",length)
print("Extracted:",data[length-1] , type(data[length-1])) # Extract (Set) in a Tuple --> {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
print(type(data[length-1]))

while (length != 0):
    for i in data[length-1]:
        print(i)
    length -= 1
print("length",length)

print("**************************************************************************************")
print("Fetching (Dictionary Items) with Two while loop")
data2 = ({"key1":1,"key2":2,"key3":3})

print("Before Convert:",data , type(data2))
length = len(data2)
print("length",length)


elms = data2.items()
length = len(data2.items())

d_items = data2.items()
newList = list(d_items)
print("newList",newList,type(newList))
print("Extracted:",newList[length-1] , type(newList[length-1]))


while (length != 0):
    
        #print(l[length-1])
        #print(type(l[length-1]))
        #print(len(l[length-1]))
        lengthInner = len(newList[length-1])
        while(lengthInner != 0):
            print(print(newList[length-1][lengthInner-1]))
            lengthInner -= 1
        length -= 1
print("length",length)
print("**************************************************************************************")
print("Fetching (Dictionary Items) with Two while loop")
data3 = ({"key1":1,"key2":2,"key3":3},)
print(data3 , type(data3))

index = 0
index_inner = 0
length_outer = len(data3)
while index<length_outer:
    #do something
    print(data3[index])

    print(len(data3[index]))

    length = len(data3[index].items())
    data_items = data3[index].items()
    print(data_items)
    newList = list(data_items)
    print("newList",newList,type(newList))
    print("Extracted:",newList[length-1] , type(newList[length-1]))
    print("Results::::::::::::::::::::::::::::")

    while (length != 0):
    
        # print(newList[length-1])
        # print(type(newList[length-1]))
        # print(len(newList[length-1]))
        lengthInner = len(newList[length-1])
        while(lengthInner != 0):
            print(print(newList[length-1][lengthInner-1]))
            lengthInner -= 1
        length -= 1

    index = index+1
#print("length",length)






