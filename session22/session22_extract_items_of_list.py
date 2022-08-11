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
                frozenset({100, "banana", True,None}),
                {1,2,3},
                {"a","b","c"},
                {"name":"davoud" , "family":"keramati"},
                {"first":{1,2,3},"second":{"a","b","c"},"third":{"name":"davoud","family":"keramati"}}
            ]
print("Access By Index of List ------------------------------------")
# List items are indexed and you can access them by referring to the index number
# Note: The first item has index 0
print(myList[0])
print(myList[1])
print(myList[2])
print(myList[3])
print("Access By Negative Indexing ------------------------------------")
print(myList[0])
print(myList[-1])
print(myList[-2])
print(myList[-3])
print("Access By Range of Indexes ------------------------------------")
print(myList[0:2])
print(myList[-1:5])
print(myList[-2:7])
print(myList[1:10])
print(myList[1:])
print(myList[:9])
print(myList[-2:])
print(myList[:-9])





