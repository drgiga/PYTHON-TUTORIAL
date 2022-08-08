# Append Items
# To add an item to the end of the list, use the append() method:


# Using the append() method to append an item:

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
print("------------------------------------")
# Insert Items
# To insert a list item at a specified index, use the insert() method.

# The insert() method inserts an item at the specified index:

# Insert an item as the second position:

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)
print("------------------------------------")
# Extend List
# To append elements from another list to the current list, use the extend() method.

# Add the elements of tropical to thislist:

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
# The elements will be added to the end of the list.
print("------------------------------------")
# Add Any Iterable
# The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).

# Add elements of a tuple to a list:

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)