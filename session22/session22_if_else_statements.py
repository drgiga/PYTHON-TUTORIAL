num = -3
if num > 0:
    print(num, "is a positive number.")

else:
    print(num, "is not a positive number.")

print("---------------------------------")
myList = ["ali","hasan","davoud","koorosh","cyrus","behnam","shervin","iran","sara","roshanak","fatemeh","fariba","sanaz","aysan"]
search_name = "alias"
if (search_name in myList):
    print(True)
else:
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
    else:
        print("Ali was not found")
        notfound = notfound + 1
        print("Not Found Items:",notfound)
print("---------------------------------")
myList2 = ["ali","hasan","davoud","koorosh","cyrus","behnam","shervin","aLI","iran","sara","roshanak","fatemeh","fariba","sanaz","aysan","Ali","Davoud"]

def itemFounder(imput_item):
    if(imput_item.lower() == "ali"):        
        print("Ali found")
    else: 
        return "Not Found"
        
for item in myList2:    
    print(itemFounder(item))


