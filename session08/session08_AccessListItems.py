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

# List items are indexed and you can access them by referring to the index number
# Note: The first item has index 0
print(myList[0])
print(myList[1])
print(myList[2])
print(myList[3])

print("Iterate List with a for Loop ------------------------------------")
# Iterate List with a for Loop
for items in myList:
    print(items)

print("Iterate List with a for Loop and Using range() function ------------------------------------")
"""
# Iterate List with a for Loop and Using range() function
# range() starts from index 0 and since lists also start from index 0, 
# so using range() function together with len() function is useful to access the elements inside the list.
"""

for items in range(len(myList)): 
    print("index:",items , "value:",myList[items])

print("Iterate List with a While Loop ------------------------------------")
# Iterate List with a While Loop
i = 0
while i < len(myList):
    print("index:",i , "value:",myList[i])
    i += 1

print("Iterate List with a While Loop ------------------------------------")
"""
# Use enumerate() to Iterate Through a Python List
# With Python’s enumerate() method you can iterate through a list or tuple 
# while accessing both the index and value of the iterable (list or tuple) object. 
# Using enumerate is similar to combining a basic for loop and a for loop that iterates by index.
# A call to enumerate() returns an enumerate object that is iterable and can be used in a loop. 
# The enumerate object contains the index and value for each element in the iterable.
"""
for i, item in enumerate(myList):
    print('index:', i, 'item:', item, 'tuple:', myList[i])

print("List Comprehension to Iterate List ------------------------------------")
"""
# Python list comprehension is a simple, concise way of iterating through lists (or tuples) to access or alter values. 
# The result of list comprehension is another list (or other iterable, like a tuple) 
# so you don’t need to write a full loop and append results to another iterable.
"""
print([item for item in myList])



