"""
There are three numeric types in Python:

int
float
complex

"""
xint = 1    # int
yfloat = 2.8  # float
zcomplex = 1j   # complex
print(type(xint),type(yfloat),type(zcomplex))
# ---------------------------------------------------------------
x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))
# ---------------------------------------------------------------
x1 = 1.10
y1 = 1.0
z1 = -35.59

print(type(x1))
print(type(y1))
print(type(z1))
# ---------------------------------------------------------------
x4 = 3+5j
y4 = 5j
z4 = -5j

print(type(x4))
print(type(y4))
print(type(z4))
# ---------------------------------------------------------------
x3 = 35e3
y3 = 12E4
z3 = -87.7e100

print(type(x3))
print(type(y3))
print(type(z3))
# ---------------------------------------------------------------
x = 1    # int
y = 2.8  # float
z = 1j   # complex
print("before convertation:",x)
print("before convertation:",y)
print("before convertation:",z)

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print("after convertation:",a)
print("after convertation:",b)
print("after convertation:",c)

print(type(a))
print(type(b))
print(type(c))
# ---------------------------------------------------------------
