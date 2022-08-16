count = 0
myList = [3, 41, 12, 9, 74, 15]
for itervar in myList:
    count = count + 1
print('Count: ', count)
print("----------------------------------")
total = 0
for itervar in [3, 41, 12, 9, 74, 15]:
    total = total + itervar
print('Total: ', total)
print("----------------------------------")
largest = None
print('Before:', largest)
for itervar in [3, 41, 12, 9, 74, 15]:
        if largest is None or itervar > largest :
            largest = itervar
        print('Loop:', itervar, largest)
print('Largest:', largest)
print("----------------------------------")
smallest = None
print('Before:', smallest)
for itervar in [3, 41, 12, 9, 74, 15]:
    if smallest is None or itervar < smallest:
        smallest = itervar
    print('Loop:', itervar, smallest)
print('Smallest:', smallest)
print("----------------------------------")
myStr = "My name is Davoud  ."
index = 0

while(index < len(myStr)):
    print("index:",index," Value:",myStr[index])
    index = index+1
print("Traversal through a string with a loop")

