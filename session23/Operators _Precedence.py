"""
Operator	                Description
:=	                        Assignment expression (Lowest precedence)
lambda	                    Lambda expression
if-else	                    Conditional expression
or	                        Boolean OR
and	                        Boolean AND
not x	                    Boolean NOT
<, <=, >, >=, 	            Comparison operators
!=, ==	                    Equality operators
in, not in, is, is not,	    Identity operators, membership operators
|	                        Bitwise OR
^	                        Bitwise XOR
&	                        Bitwise AND
<<, >>	                    Left and right Shifts
+, –	                    Addition and subtraction
*, @, /, //, %	            Multiplication, matrix multiplication, division, floor division, remainder
+x, -x, ~x	                Unary plus, Unary minus, bitwise NOT
**	                        Exponentiation
await                       x	Await expression
--------------------------- Subscription, slicing, call, attribute reference
x[index],                   Subscription
x[index:index],             slicing
x(arguments…),              call
x.attribute                 attribute reference
--------------------------- Binding or parenthesized expression, list display, dictionary display, set display
(expressions…),             Binding or parenthesized expression
[expressions…],             list display
{key: value…},              dictionary display
{expressions…}              set display
---------------------------
()	Parentheses             (Highest precedence)
"""
expression = 1+2*6**3//2/3-1
print(expression)