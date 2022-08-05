# for example for person

name = "davoud"
lastName = "keramati"
age = 35
phone = "09121234567"
tel = "44425698"
country = "iran"
city = "tehran"
address = "saadat abad - sarv - block 14"
height = 178.59
weight = 84.56

# for example otherInfo , otherInfo2 , person , person2 are Dictionary
otherInfo  = {"job":"programmer", "education":"msc artificial intelligence", "score":100 , "complexNum":3j+1e27 ,"isStudent":False ,"haveChild":None} # dict
otherInfo2  = {'job':"programmer", 'education':"msc artificial intelligence", 'score':100 , "complexNum":-3j-1e27,"isStudent":True , 'havechild':None} # dict
person = {
    'name' : name,
    'lastName' : lastName,
    'age' : age,
    'phone' : phone,
    'tel' : tel,
    'country' : country,
    'city' : city,
    'address' : address,
    'height' : height,
    'weight' : weight,
    'otherInfo' :otherInfo,
    'otherInfo2' : otherInfo2
} # dict
print(person)
print(type(person))
print(len(person))

person2 = {
    "name" : name,
    "lastName" : lastName,
    "age" : age,
    "phone" : phone,
    "tel" : tel,
    "country" : country,
    "city" : city,
    "address" : address,
    "height" : height,
    "weight" : weight,
    "otherInfo" :otherInfo,
    "otherInfo2" : otherInfo2
} # dict

print(person2)
print(type(person2))
print(len(person2))
