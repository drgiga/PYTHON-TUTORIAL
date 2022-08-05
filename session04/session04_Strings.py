str1 = "Hello World" # String
str2 = 'Hello World' # String
str3 = 'a'
str4 = "a"
print(type(str1))
print(type(str2))
print(type(str3))
print(type(str4))
print('-----------------------------------')
print("-----------------------------------")
person1 = "davoud" 
person2 = "ali"
sentence1 = "i am a programmer" 
sentence2 = "i am a teacher" 

print('in this dialog' ,person1,'said: ',sentence1)
print('in this dialog' ,person2,'said: ',sentence2)

print(f'in this dialog' ,person1,'said: ',sentence1)
print(f'in this dialog' ,person2,'said: ',sentence2)

print(f'in this dialog {person1}said: {sentence1}')
print(f"in this dialog {person2}said: {sentence2}")


print('-----------------------------------')
print('in this dialog davoud is said: "i am a programmer" ')
print("in this dialog ali is said: 'i am a teacher'")
print('-----------------------------------')
print('in this dialog davoud is said: \'i am a programmer\' ')
print("in this dialog ali is said: \"i am a teacher\" ")
print('-----------------------------------')
print("in this \n dialog ali is \n said: \"i am a teacher\" ")
print('-----------------------------------')
print("in this \\ dialog ali is \\ said: \"i am a teacher\" ")
print('-----------------------------------')
myName = "davoud"
myFamily = "rahmati"

print(myName+myFamily)
print(myName+' '+myFamily)
print(myName+" "+myFamily)
print(myName,myFamily) # in this case symbol (,) equals with ' ' epmty space

# print(myName+" "+myFamily+1000) # TypeError: can only concatenate str (not "int") to str
print(str(1000)) # Convert integer to string

convertedVar = str(1000)
print(convertedVar)
print(myName+" "+myFamily+convertedVar) # without Error

print(myName+" "+myFamily,1000) # without Error

#convertedVar2 += str(1000) # NameError: name 'convertedVar2' is not defined. Did you mean: 'convertedVar'?
#print(convertedVar2)

convertedVar2 = str(1000)
print(convertedVar2)

print('-----------------------------------')
# Multiline Strings
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
print('-----------------------------------')
a1 = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a1)
print('-----------------------------------')
