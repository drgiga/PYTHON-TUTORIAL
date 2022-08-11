myList = [
                {"name":"davoud" , "family":"keramati","age":35,"complex":-1+5j,"isLive":True,"None":None,"float":654.8520},
                "My Name Is Davoud",
                ['My Name','Is','Davoud'],
                {1.0,"Hello",145,-1j,3j+8,'world',False,True,None},
                [{1.0,"Hello",145,-1j,3j+8,'world',False,True,None} , {123,85.54,True,None,"rtretert"}],
                False,
                584.5487,
                None,
                {"one","two","three"},
                [None],
                [{1,2,3},{"a","b","c"},{"name":"davoud" , "family":"keramati"}],
                frozenset({"apple", "banana", "cherry"}),
                frozenset({"100", "banana", "True","None"}),
                {1,2,3},
                {"a","b","c"},
                {"name":"davoud" , "family":"keramati"},
                {"first":{1,2,3},"second":{"a","b","c"},"third":{"name":"davoud","family":"keramati"}}
            ]


print("Iterate List with a for Loop ------------------------------------")
# Iterate List with a for Loop
sets_counter = 0
sets_container = {None}

lists_counter = 0
lists_container = []

dicts_counter = 0
dicts_container = {}

result = None
temp = ""
counter = 0
temp2 = None
temp3 = None
temp4 = None
# frozenSets_container = frozenset({})

for items in myList:
    print(items)
    if(type(items) == set):
        sets_counter = sets_counter + 1
        sets_container.update(items)
    elif(type(items) == list):
        lists_counter = lists_counter + 1
        lists_container.append(items)
    elif(type(items) == dict):
        dicts_counter = dicts_counter + 1
        dicts_container.update(items)
    elif(type(items) == frozenset): 
        #type1 = type(items)
        temp = (items , temp)
        result = temp
        counter += 1
        """for i in range(len(result)):
            temp2 = result[i]
            for ii in temp2:
                temp3 = type(ii)
                #temp4 = temp2[ii]
                temp4 = list(temp2)"""
        
        
        
        

print("sets:-------------------")
print(sets_counter)
print(sets_container)
print("lists:------------------")
print(lists_counter)
print(lists_container)
print("dicts:------------------")
print(dicts_counter)
print(dicts_container)
print("frozensets:------------------")
print(counter)
print(result)
print(type(result))
print("temp2",temp2)
print(temp3)
print(temp4)


print("Result:",result)
print("result type:",type(result))
for x in result:
    print(x)
    for xin in x:
        print(xin)
        for yin in xin:
            print(yin)


