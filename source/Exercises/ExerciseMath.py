"""
math.acos()	Returns the arc cosine of a number
math.acosh()	Returns the inverse hyperbolic cosine of a number
math.asin()	Returns the arc sine of a number
math.asinh()	Returns the inverse hyperbolic sine of a number
math.atan()	Returns the arc tangent of a number in radians
math.atan2()	Returns the arc tangent of y/x in radians
math.atanh()	Returns the inverse hyperbolic tangent of a number
math.ceil()	Rounds a number up to the nearest integer
math.comb()	Returns the number of ways to choose k items from n items without repetition and order
math.copysign()	Returns a float consisting of the value of the first parameter and the sign of the second parameter
math.cos()	Returns the cosine of a number
math.cosh()	Returns the hyperbolic cosine of a number
math.degrees()	Converts an angle from radians to degrees
math.dist()	Returns the Euclidean distance between two points (p and q), where p and q are the coordinates of that point
math.erf()	Returns the error function of a number
math.erfc()	Returns the complementary error function of a number
math.exp()	Returns E raised to the power of x
math.expm1()	Returns Ex - 1
math.fabs()	Returns the absolute value of a number
math.factorial()	Returns the factorial of a number
math.floor()	Rounds a number down to the nearest integer
math.fmod()	Returns the remainder of x/y
math.frexp()	Returns the mantissa and the exponent, of a specified number
math.fsum()	Returns the sum of all items in any iterable (tuples, arrays, lists, etc.)
math.gamma()	Returns the gamma function at x
math.gcd()	Returns the greatest common divisor of two integers
math.hypot()	Returns the Euclidean norm
math.isclose()	Checks whether two values are close to each other, or not
math.isfinite()	Checks whether a number is finite or not
math.isinf()	Checks whether a number is infinite or not
math.isnan()	Checks whether a value is NaN (not a number) or not
math.isqrt()	Rounds a square root number downwards to the nearest integer
math.ldexp()	Returns the inverse of math.frexp() which is x * (2**i) of the given numbers x and i
math.lgamma()	Returns the log gamma value of x
math.log()	Returns the natural logarithm of a number, or the logarithm of number to base
math.log10()	Returns the base-10 logarithm of x
math.log1p()	Returns the natural logarithm of 1+x
math.log2()	Returns the base-2 logarithm of x
math.perm()	Returns the number of ways to choose k items from n items with order and without repetition
math.pow()	Returns the value of x to the power of y
math.prod()	Returns the product of all the elements in an iterable
math.radians()	Converts a degree value into radians
math.remainder()	Returns the closest value that can make numerator completely divisible by the denominator
math.sin()	Returns the sine of a number
math.sinh()	Returns the hyperbolic sine of a number
math.sqrt()	Returns the square root of a number
math.tan()	Returns the tangent of a number
math.tanh()	Returns the hyperbolic tangent of a number
math.trunc()	Returns the truncated integer parts of a number

Constants:

math.e	Returns Euler's number (2.7182...)
math.inf	Returns a floating-point positive infinity
math.nan	Returns a floating-point NaN (Not a Number) value
math.pi	Returns PI (3.1415...)
math.tau	Returns tau (6.2831...)
"""

print("Importing the math module and using some of its functions and constants:")
print("---------------------------------------------------------------")
import math
print(f"math.pi: {math.pi}")
print(f"math.e: {math.e}")
print(f"math.sqrt(16): {math.sqrt(16)}")
print(f"math.factorial(5): {math.factorial(5)}")
print(f"math.log(100, 10): {math.log(100, 10)}")
print(f"math.sin(math.radians(90)): {math.sin(math.radians(90))}")
print(f"math.ceil(4.3): {math.ceil(4.3)}")
print(f"math.floor(4.7): {math.floor(4.7)}")
print(f"math.gcd(48, 180): {math.gcd(48, 180)}") # Greatest Common Divisor
print(f"math.isfinite(10): {math.isfinite(10)}") # Check if finite
print(f"math.isinf(math.inf): {math.isinf(math.inf)}") # Check if infinite
print(f"math.isnan(math.nan): {math.isnan(math.nan)}") # Check if NaN
print("---------------------------------------------------------------")
print("You can explore more functions and constants in the math module documentation.")
print("---------------------------------------------------------------")

numeros = [1, 2, 3, 4, 5]
print(f"e o maior número da lista {numeros} é {max(numeros)}")
print(f"e o menor número da lista {numeros} é {min(numeros)}")
print(f"a soma de todos os números da lista {numeros} é {sum(numeros)}")
print(f"a soma de todos os números da lista {numeros} usando math.fsum é {math.fsum(numeros)}")
print("---------------------------------------------------------------")
print("A potência de 2 elevado a 3 é:", pow(2, 3)) # 2^3 = 8
print("A potência de 3 elevado a 4 é:", math.pow(3, 4)) # 3^4 = 81.0
print("---------------------------------------------------------------")
print(f"{abs(-10)} é o valor absoluto de -10")