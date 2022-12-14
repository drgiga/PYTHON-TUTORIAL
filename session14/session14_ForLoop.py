# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
fruitsList = ["apple", "banana", "cherry"]
for x in fruitsList:
  print(x)
print("------------------ Looping Through a String ----------------")
# Looping Through a String
# Even strings are iterable objects, they contain a sequence of characters:
# Loop through the letters in the word "banana":
for x in "banana":
  print(x)
print("------------------ The break Statement ----------------")
"""
# The break Statement
With the break statement we can stop the loop before it has looped through all the items:
"""
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
print("------------------ The break Statement ----------------")
# Exit the loop when x is "banana", but this time the break comes before the print:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)
print("------------------ The continue Statement ----------------")
# The continue Statement
# With the continue statement we can stop the current iteration of the loop, and continue with the next:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
print("------------------ The range() Function ----------------")
"""
# The range() Function
To loop through a set of code a specified number of times, we can use the range() function,
The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.
"""
for x in range(6):
  print(x)
print("------------------ The range() Function ----------------")
for x in range(2, 6):
  print(x)
print("------------------ The range() Function ----------------")
"""
# The range() function defaults to increment the sequence by 1, 
# however it is possible to specify the increment value by adding a third parameter: range(2, 30, 3):
"""
for x in range(2, 30, 3):
  print(x)
print("----------------- Else in For Loop -----------------")
# Else in For Loop
# The else keyword in a for loop specifies a block of code to be executed when the loop is finished:
# Print all numbers from 0 to 5, and print a message when the loop has ended:
for x in range(6):
  print(x)
else:
  print("Finally finished!")
print("----------------- Else in For Loop -----------------")
# Note: The else block will NOT be executed if the loop is stopped by a break statement.
# TBreak the loop when x is 3, and see what happens with the else block:
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")
print("----------------- Nested Loops -----------------")
# A nested loop is a loop inside a loop.
# The "inner loop" will be executed one time for each iteration of the "outer loop":
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
print("----------------- The pass Statement -----------------")
# for loops cannot be empty, but if you for some reason have a for loop with no content, put in the pass statement to avoid getting an error.
for x in [0, 1, 2]:
  pass
print("----------------- Fetching the members of a Set through iteration  -----------------")
fruitsSet = {"apple", "banana", "cherry"}
for x in fruitsSet:
  print(x)
print("----------------- Fetching the members of a FrozenSet through iteration  -----------------")
fruitsFrozenSet = frozenset({"apple", "banana", "cherry"})
for x in fruitsFrozenSet:
  print(x)
print("----------------- Fetching the members of a Tuple through iteration  -----------------")
fruitsTuple = ("apple", "banana", "cherry")
for x in fruitsTuple:
  print(x)
print("----------------- Fetching the members of a Dictionary through iteration  -----------------")
fruitsDictionary = {"val1":"apple", "val2":"banana", "val3":"cherry"}
for x in fruitsDictionary:
  print(x)
  print(fruitsDictionary[x])
print("----------------- Fetching the members of a Dictionary through iteration  -----------------")
fruitsDictionary = {"val1":"apple", "val2":"banana", "val3":"cherry"}
for key in fruitsDictionary:
  print(key)
  print(fruitsDictionary[key])
print("----------------- Fetching the members of a Dictionary through iteration  -----------------")
fruitsDictionary = {"val1":"apple", "val2":"banana", "val3":"cherry"}
for key in fruitsDictionary:
  print(key,fruitsDictionary[key])
print("----------------- Fetching the members of a Dictionary through iteration  -----------------")
fruitsDictionary = {"val1":"apple", "val2":"banana", "val3":"cherry"}
for key in fruitsDictionary:
  print(key+":"+fruitsDictionary[key])

