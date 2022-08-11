num = -3
if num > 0:
    print(num, "is a positive number.")

elif num < 0:
    print(num, "is a positive number.")

print("---------------------------------")
myList = ["ali","hasan","davoud","koorosh","cyrus","behnam","shervin","iran","sara","roshanak","fatemeh","fariba","sanaz","aysan"]
search_name = "alias"
if (search_name in myList):
    print(True)
elif (True != (search_name in myList)):
    print(False)
print("---------------------------------")
myList = ["ali","hasan","davoud","koorosh","cyrus","behnam","shervin","aLI","iran","sara","roshanak","fatemeh","fariba","sanaz","aysan","Ali","Davoud"]

found = 0
notfound = 0
for item in myList:    
    if(item.lower() == "ali"):        
        print("Ali was found")
        found = found + 1
        print("Found Items:",found)
    elif(item.lower()!= "ali"):
        print("Ali was not found")
        notfound = notfound + 1
        print("Not Found Items:",notfound)
