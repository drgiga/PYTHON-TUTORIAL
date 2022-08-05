myStringFrozenSet = frozenset({"apple", "banana", "cherry"})	# frozenset	
myStringFrozenSet2 = frozenset({"apple", "banana", "cherry"})	# frozenset	
print(type(myStringFrozenSet))
print(type(myStringFrozenSet2))

myStringFrozenSet3 = frozenset({"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"})  # frozenset
print(type(myStringFrozenSet3))

myIntegerFrozenSet = frozenset({-1,2,100,854210,-659875123354,999999999999999999999999999}) # frozenset
print(type(myIntegerFrozenSet))

myFloatFrozenSet = frozenset({1.0,-2.0,-100.450,854210.548,659875123354.5124,999999999999999999999999999.0101010,-999999999999999999999999999.0101010}) # frozenset
print(type(myFloatFrozenSet))

myAllTypeFrozenSet = frozenset({1.0,"Hello",145,-1j,3j+8,'world',False,True,None}) # frozenset
print(type(myAllTypeFrozenSet))

print(myStringFrozenSet)
print(myStringFrozenSet2)
print(myStringFrozenSet3)
print(myIntegerFrozenSet)
print(myFloatFrozenSet)
print(myAllTypeFrozenSet)

# len() method/function for calculate length of frozenset
print(len(myStringFrozenSet))
print(len(myStringFrozenSet2))
print(len(myStringFrozenSet3))
print(len(myIntegerFrozenSet))
print(len(myFloatFrozenSet))
print(len(myAllTypeFrozenSet))