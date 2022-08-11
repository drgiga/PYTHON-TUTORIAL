numbers = range(0,100)
for num in numbers:
    if (num %2 == 0):
        print(num , "is even")
    else:
        print(num , "is odd")

print("---------------------------------")
myList = ["ali","hasan","davoud","koorosh","cyrus","behnam","shervin","aLI","iran","sara","roshanak","fatemeh","fariba","sanaz","aysan","Ali","Davoud"]

found = 0
notfound = 0
for item in myList:    
    if(item.lower() == "ali"):        
        print("Ali was found")
        found = found + 1
        
    else:
        print("Ali was not found")
        notfound = notfound + 1
print("Results:---------------------")        
print("Found Items:",found)       
print("Not Found Items:",notfound)
print("---------------------------------")
mySet = {"ali","hasan","davoud","koorosh","cyrus","behnam","shervin","aLI","iran","sara","roshanak","fatemeh","fariba","sanaz","aysan","Ali","Davoud"}

found = 0
notfound = 0
for item in mySet:    
    if(item.lower() == "ali"):        
        print("Ali was found")
        found = found + 1
        
    else:
        print("Ali was not found")
        notfound = notfound + 1
print("Results:---------------------")        
print("Found Items:",found)       
print("Not Found Items:",notfound)
print("---------------------------------")

data = [
    {'Name': 'Bobby', 'Id': 1, "Age": 20},
    {'Name': 'ojaswi', 'Id': 2, "Age": 22},
    {'Name': 'rohith', 'Id': 3, "Age": 20},
]
for i in data:
    for key , value in i.items():
        # display
        # print(i)
        print(key,value)
        for i in key:
            print(key,value)

