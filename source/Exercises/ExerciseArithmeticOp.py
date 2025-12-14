x = 15
y = 4

print(x + y) # Addition
print(x - y) # Subtraction
print(x * y) # Multiplication
print(x / y) # Division
print(x % y) # Modulus
print(x ** y) # Exponentiation
print(x // y) # Floor Division. Floor division always returns an integer. It rounds DOWN to the nearest integer:

x += 5
print(x)

x -= 3
print(x)

x *= 2
print(x)

x /= 4
print(x)

x %= 3
print(x)

x **= 2
print(x)

x //= 4
print(x)

print("Funções concluídas.")

x = 5

x &= 2 # AND
print(x) # 0

x ^= 3 # XOR
print(x) # 3

x |=4 # OR
print(x) # 7

x >>= 1 # Right shift
print(x) # 3

x <<= 2 # Left shift
print(x) # 12

print(x := 5) # Assignment expression (walrus operator)

numbers = [1, 2, 3, 4, 5]
count = len(numbers)
if count > 3:
    print(f"List has {count} elements") # Traditional way

if (count := len(numbers)) > 3:
    print(f"List has {count} elements") # Using assignment expression

x = 5
y = 3

print(x == y) # Equality
print(x != y) # Inequality
print(x > y) # Greater than
print(x < y) # Less than
print(x >= y) # Greater than or equal to
print(x <= y) # Less than or equal to

x = 5

print(1 < x < 10) # Chained comparison

print(1 < x and x < 10) # Equivalent to chained comparison

x = 5

print(not(x > 3 and x < 10))

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z) # Identity
print(x is y) # x and y have same content but are different objects
print(x == y) # x and y have same content

x = ["apple", "banana"]
y = ["apple", "banana"]

print(x is not y) # x and y are different objects
print(x != y) # x and y have same content

"""
is - Checks if both variables point to the same object in memory
== - Checks if the values of both variables are equal
is not - Checks if both variables do not point to the same object in memory
!= - Checks if the values of both variables are not equal
"""

fruits = ["apple", "banana", "cherry"]

print("banana" in fruits) # Membership

fruits = ["apple", "banana", "cherry"]

print("pineapple" not in fruits) # Membership

text = "Hello World"

print("H" in text) # Membership
print("hello" in text)
print("z" not in text)

print(6 & 3) # AND

print(100 + 5 * 3) # Multiplication has higher precedence than addition

"""
()	Parentheses	
**	Exponentiation	
+x  -x  ~x	Unary plus, unary minus, and bitwise NOT	
*  /  //  %	Multiplication, division, floor division, and modulus	
+  -	Addition and subtraction	
<<  >>	Bitwise left and right shifts	
&	Bitwise AND	
^	Bitwise XOR	
|	Bitwise OR	
==  !=  >  >=  <  <=  is  is not  in  not in 	Comparisons, identity, and membership operators	
not	Logical NOT	
and	AND	
or	OR
"""

print(5 + 4 - 7 + 3) # Left to right