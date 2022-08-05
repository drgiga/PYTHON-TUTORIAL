name = "Davoud"
lastName = "Keramati"
age = 36
txt = "My Full Name is: {} {}, and I am {}"
print(txt.format(name,lastName,age))
print("--------------------------------")
quantity = 3 # 0 Because a string array starts from index 0
itemno = 567 # 1
price = 49.95 # 2
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))
print("--------------------------------")
professions = ["java","javascript","python"]
firs_name = "Hadi"
last_name = "Rahmati"
myInfo = "My name is {1} {2} , My Job Professions are: {0} ."

print(myInfo.format(professions,firs_name,last_name))