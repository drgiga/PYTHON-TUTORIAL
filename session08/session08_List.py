stringList = ["apple", "banana", "cherry", "apple", "cherry"," "]
print(stringList)

stringList2 = ['apple', 'banana', 'cherry', 'apple', 'cherry',' ']
print(stringList2)

integerList = [1,200,89754520,999999999999999999999999999999999999999999999999999,0]
floatList = [1.0,20058.02154,897.54520,999999999999999999999999999999999999999999999999999.02020202,0.0]
complexList = [1j+8,-2j+74,7+3j,3+6j]
booleanList = [True,True,False,True,False,False]
listOfSets = [
                {"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"},
                {"My Name","Is","Davoud"},{'My Name','Is','Davoud'},
                {1,-200,3,-454,59854,-6,},{1j+8,-2j+74,7+3j,3+6j},
                {True,True,False,True,False,False},
                {1.0,-20058.02154,-897.54520,8751924.699999},
                {None,None,None,None,None,None,None},
                {1.0,"Hello",145,-1j,3j+8,'world',False,True,None}
            ]
listOfLists = [
                ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"],
                ["My Name","Is","Davoud"],
                ['My Name','Is','Davoud'],
                [1,-200,3,-454,59854,-6,],
                [1j+8,-2j+74,7+3j,3+6j],
                [True,True,False,True,False,False],
                [1.0,-20058.02154,-897.54520,8751924.699999],
                [None,None,None,None,None,None,None],
                [1.0,"Hello",145,-1j,3j+8,'world',False,True,None]
            ]
listOfDictionaries = [
                {"name":"davoud" , "family":"keramati","age":35,"complex":-1+5j,"isLive":True,"None":None,"float":654.8520},
                {"1":"My Name","2":"Is","3":"Davoud"},
                {"1":'My Name',"2":'Is',"3":'Davoud'},
                {"1":1,"2":-200,"3":-454,"4":59854,"index":-6},
                {1j+8,-2j+74,7+3j,3+6j},
                {True,True,False,True,False,False},
                {1.0,-20058.02154,-897.54520,8751924.699999},
                {None,None,None,None,None,None,None},
                {1.0,"Hello",145,-1j,3j+8,'world',False,True,None}
            ]
listOfAllTypes = [
                {"name":"davoud" , "family":"keramati","age":35,"complex":-1+5j,"isLive":True,"None":None,"float":654.8520},
                "My Name Is Davoud",
                ['My Name','Is','Davoud'],
                {1.0,"Hello",145,-1j,3j+8,'world',False,True,None},
                [{1.0,"Hello",145,-1j,3j+8,'world',False,True,None} , {123,85.54,True,None,"rtretert"}],
                False,
                584.5487,
                None
            ]
listOfAllTypes2 = [
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

print("------------------------------------")
print(stringList)
print(stringList2)
print(integerList)
print(floatList)
print(complexList)
print(booleanList)
print("------------------------------------")
print(listOfSets)
print("------------------------------------")
print(listOfLists)
print("------------------------------------")
print(listOfDictionaries)
print("------------------------------------")
print(listOfAllTypes)
print("------------------------------------")
print(listOfAllTypes2)
print("------------------------------------")
print(listOfAllTypes2[1])
print("------------------------------------")
print(listOfAllTypes2[-1])
print("------------------------------------")
print(listOfAllTypes2[2:5])
print("------------------------------------")
print(listOfAllTypes2[:4])
print("------------------------------------")
print(listOfAllTypes2[2:])