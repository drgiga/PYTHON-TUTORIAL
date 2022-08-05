myStringSet = {"apple", "banana", "cherry"}	# set
myStringSet2 = {'apple', 'banana', 'cherry'} # set

myStringSet3 = {"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"}
print(type(myStringSet3))

myIntegerSet = {-1,2,100,854210,-659875123354,999999999999999999999999999}
print(type(myIntegerSet))

myFloatSet = {1.0,-2.0,-100.450,854210.548,659875123354.5124,999999999999999999999999999.0101010,-999999999999999999999999999.0101010}
print(type(myFloatSet))

myAllTypeSet = {1.0,"Hello",145,-1j,3j+8,'world',False,True,None}
print(type(myAllTypeSet))

print(myStringSet)
print(myStringSet2)
print(myStringSet3)
print(myIntegerSet)
print(myFloatSet)
print(myAllTypeSet)

# len() method/function for calculate length of set
print(len(myStringSet))
print(len(myStringSet2))
print(len(myStringSet3))
print(len(myIntegerSet))
print(len(myFloatSet))
print(len(myAllTypeSet))