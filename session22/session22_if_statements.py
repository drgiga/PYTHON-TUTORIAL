num = 3
if num > 0:
    print(num, "is a positive number.")
print("This is always printed.")

num = -1
if num > 0:
    print(num, "is a positive number.")
print("This is also always printed.")
print("---------------------------------")
myList = ["ali","hasan","davoud","koorosh","cyrus","behnam","shervin","iran","sara","roshanak","fatemeh","fariba","sanaz","aysan"]
if ("ali" in myList):
    print(True)
print("---------------------------------")
myList = ["ali","hasan","davoud","koorosh","cyrus","behnam","shervin","aLI","iran","sara","roshanak","fatemeh","fariba","sanaz","aysan","Ali","Davoud"]

found = 0
for item in myList:    
    if(item.lower() == "ali"):        
        print("Ali was found")
        found = found + 1

print("Found Items:",found)    
