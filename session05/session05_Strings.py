# strings in Python are arrays of bytes
myProfessions = ["Computer Programmer","Front-End Developer","Full-Stack Developer","Software Application Developer","Computer Systems Analyst"]
myInfo = f"My name is Davoud Keramati. My Job Professions are: {myProfessions}" # myInfo is a String Variable & is a array of bytes

print("myInfo",myInfo)
print("--------------------------------")
print(type(myInfo))
print("--------------------------------")
print(type(myInfo[0]))

print(myInfo[0])
print(myInfo[1])
print(myInfo[2])
print(myInfo[3])
print(myInfo[4])
print(myInfo[5])
print("--------------------------------")
print(len(myInfo)) # Get Length of String Array (myInfo)
"""
The output in the while loop shows that strings in Python are arrays
"""
iterator=0

while iterator < len(myInfo):
    print(myInfo[iterator])
    iterator += 1

print("--------------------------------")
# Check String in a Text
#sample 1
txt = "The best things in life are free!"
print("free" in txt) # Output is {True or False}

#sample 2
if "free" in txt:
  print("Yes, 'free' is present.")

#sample 3
print("expensive" not in txt) # Output: True
print("free" not in txt) # Output: False

#sample 4
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")
