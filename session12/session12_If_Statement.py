a = 33
b = 200
if b > a:
  print("b is greater than a")
print("------------------------------------")
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
print("------------------------------------")
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
print("------------------------------------")
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
print("------------------------------------")
if a > b: print("a is greater than b")
print("------------------------------------")
print("A") if a > b else print("B")
print("------------------------------------")
print("A") if a > b else print("=") if a == b else print("B")
print("------------------------------------")
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")
print("------------------------------------")
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")
print("------------------------------------")
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")
print("------------------------------------")
a = 33
b = 200

if b > a:
  pass
print("------------------------------------")
person1 = {"name":"Davoud",
          "family":"Keramati",
          "age":"35",
          "married":True,
          "isStuding":True,
          "hasJob":False,
          "twitter":None
          }
person2 = {"name":"Ali",
          "family":"Faraji",
          "age":"41",
          "married":True,
          "isStuding":False,
          "hasJob":False,
          "twitter":True
          }
if person1["name"] == person2["name"]:
  print("Two Names Are Equal.")
else:
  print("Two Names Are Not Equal.")
print("------------------------------------")
if person1["age"] == person2["age"]:
  print("Two Ages Are Equal.")
elif person1["age"] > person2["age"]:
  print("Age Person1 > Age Person2")
else:
  print("Age Person1 < Age Person2")