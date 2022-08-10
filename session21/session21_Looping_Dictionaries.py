from turtle import xcor


myDict = {"name":"Davoud","family":"Keramati" ,"city":'Tehran',"isMarried":True,"hasChild":None,"money":2000,"complex":1+3j,"score1":-9800,"score2":-56.541,"score3":0}

for key , value in myDict.items():
    print(key)
    print("-------------------------")
    print(value)
    print("-------------------------")
    print(key,value)
print("******************************")
thisdict =	{"name":"Davoud","family":"Keramati" ,"city":'Tehran',"isMarried":True,"hasChild":None,"money":2000,"complex":1+3j,"score1":-9800,"score2":-56.541,"score3":0}
for x in thisdict.values():
    print(x)
print("******************************")
thisdict =	{"name":"Davoud","family":"Keramati" ,"city":'Tehran',"isMarried":True,"hasChild":None,"money":2000,"complex":1+3j,"score1":-9800,"score2":-56.541,"score3":0}
for x in thisdict.keys():
    print(x)   