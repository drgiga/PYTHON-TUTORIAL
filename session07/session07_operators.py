"""
Python divides the operators in the following groups:

    Arithmetic operators
    Assignment operators
    Comparison operators
    Logical operators
    Identity operators
    Membership operators
    Bitwise operators
"""
num1 = 10
num2 = 33
result = None

"""
Python Arithmetic Operators
Arithmetic operators are used with numeric values to perform common mathematical operations:

Operator	Name	Example	Try it
+	Addition	x + y	
-	Subtraction	x - y	
*	Multiplication	x * y	
/	Division	x / y	
%	Modulus	x % y	
**	Exponentiation	x ** y	
//	Floor division	x // y
"""
result = num1+num2
print(result)
result = num1-num2
print(result)
result = num1*num2
print(result)
result = num1/num2
print(result)
result = num1%num2
print(result)
result = num1**num2
print(result)
result = num1//num2
print(result)
print('-----------------------------------')
"""
Python Assignment Operators
Assignment operators are used to assign values to variables:

Operator	Example	Same As	Try it
=	x = 5	x = 5	
+=	x += 3	x = x + 3	
-=	x -= 3	x = x - 3	
*=	x *= 3	x = x * 3	
/=	x /= 3	x = x / 3	
%=	x %= 3	x = x % 3	
//=	x //= 3	x = x // 3	
**=	x **= 3	x = x ** 3	
&=	x &= 3	x = x & 3	
|=	x |= 3	x = x | 3	
^=	x ^= 3	x = x ^ 3	
>>=	x >>= 3	x = x >> 3	
<<=	x <<= 3	x = x << 3
"""
number1 = 53
print(number1)
number1 += 6
print(number1)
number1 -= 2
print(number1)
number1 *= 12
print(number1)
number1 /= 2
print(number1)
number1 %= 6
print(number1)
# number1 //= 3
print(number1)
# number1 **= 3
print(number1)
# number1 &= 6
print(number1)
# number1 |= 6
print(number1)
# number1 ^= 6
print(number1)
# number1 >>= 6
print(number1)
# number1 <<= 6
print(number1)
print('-----------------------------------')
"""
Python Comparison Operators
Comparison operators are used to compare two values:

Operator	Name	Example	Try it
==	Equal	x == y	
!=	Not equal	x != y	
>	Greater than	x > y	
<	Less than	x < y	
>=	Greater than or equal to	x >= y	
<=	Less than or equal to	x <= y
"""
print(12 == 18)
print(12 != 18)
print(12 > 18)
print(12 < 18)
print(12 >= 18)
print(12 <= 18)

print(18 >= 18)
print(12 <= 12)
print('-----------------------------------')
"""
Python Logical Operators
Logical operators are used to combine conditional statements:

Operator	Description	Example	Try it
and 	Returns True if both statements are true	x < 5 and  x < 10	
or	Returns True if one of the statements is true	x < 5 or x < 4	
not	Reverse the result, returns False if the result is true	not(x < 5 and x < 10)
"""
print(18 >= 18 and 12 <= 12)
print(18 >= 18 or 12 <= 12)

print(not(18 >= 18 and 12 <= 12))
print(not(18 >= 50 or 12 <= 3))

print(not(None))
print(not(not(None)))
print('-----------------------------------')
"""
Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:

Operator	Description	Example	Try it
is 	Returns True if both variables are the same object	x is y	
is not	Returns True if both variables are not the same object	x is not y
"""
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z , ": because is in the same memory location")

# returns True because z is the same object as x

print(x is y , ": because is not in the same memory location")

# returns False because x is not the same object as y, even if they have the same content

print(x == y , ": because x is equal to y")

# to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y
print('-----------------------------------')
"""
Python Membership Operators
Membership operators are used to test if a sequence is presented in an object:

Operator	Description	Example	Try it
in 	Returns True if a sequence with the specified value is present in the object	x in y	
not in	Returns True if a sequence with the specified value is not present in the object	x not in y
"""
x = ["apple", "banana"]

print("banana" in x)
print("banana" not in x)
print('-----------------------------------')
"""
Python Bitwise Operators
Bitwise operators are used to compare (binary) numbers:

Operator	Name	Description
& 	AND	Sets each bit to 1 if both bits are 1
|	OR	Sets each bit to 1 if one of two bits is 1
^	XOR	Sets each bit to 1 if only one of two bits is 1
~ 	NOT	Inverts all the bits
<<	Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off
>>	Signed right shift	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off

"""
a = 10
b = 4
# Print bitwise AND operation
print("a & b =", a & b)
# Print bitwise OR operation
print("a | b =", a | b)
# Print bitwise NOT operation
print("~a =", ~a)
# print bitwise XOR operation
print("a ^ b =", a ^ b)
# Zero fill left shift
print("a << b =", a << b)
# Signed right shift
print("a >> b =", a >> b)
print("--------------------------------")