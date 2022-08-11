num = -3
if num > 0:
    print(num, "is a positive number.")

elif num == 0:
    print(num, "is egual 0")
else:
    print("is a negative number.")
print("---------------------------------")
myList = ["ali","hasan","davoud","koorosh","cyrus","behnam","shervin","iran","sara","roshanak","fatemeh","fariba","sanaz","aysan"]
search_name = "alias"
if (search_name in myList):
    print(True)
elif (True != (search_name in myList)):
    print(False)
else:
    print("This statement will never happen")
print("---------------------------------")
myList = ["ali","hasan","davoud","koorosh","cyrus","behnam","shervin","aLI","iran","sara","roshanak","fatemeh","fariba","sanaz","aysan","Ali","Davoud"]
eguals = 0
greater = 0
less = 0
lengthOfItem = 5
for item in myList:    
    if(len(item) == lengthOfItem):        
        print(f"length is equal {lengthOfItem}")
        eguals += 1
    elif(len(item) > lengthOfItem):
        print(f"length is greater than {lengthOfItem}")
        greater += 1
    else:
        print(f"length is less than {lengthOfItem}")
        less += 1
print("Results:")
print("Number of equals:",eguals)
print("Number of greater:",greater)
print("Number of less:",less)
        