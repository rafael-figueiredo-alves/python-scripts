"""
A function is a block of code which only runs when it is called.

A function can return data as a result.

A function helps avoiding code repetition.
"""

def greet(name):
    """Returns a greeting message for the given name."""
    return f"Hello, {name}!"

def add(a, b):
    """Returns the sum of two numbers."""
    return a + b

def factorial(n):
    """Returns the factorial of a number."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def is_even(number):
    """Returns True if the number is even, False otherwise."""
    return number % 2 == 0

def fibonacci(n):
    """Returns the nth Fibonacci number."""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def square(number):
    """Returns the square of a number."""
    return number * number

def reverse_string(s):
    """Returns the reverse of the given string."""
    return s[::-1]

def max_of_two(a, b):
    """Returns the maximum of two numbers."""
    return a if a > b else b

print(greet("Alice")) # Should print: Hello, Alice!
print(add(5, 3)) # Should print: 8
print(factorial(5)) # Should print: 120
print(is_even(4)) # Should print: True (é par?)
print(fibonacci(6)) # Should print: 8
print(square(7)) # Should print: 49
print(reverse_string("hello")) # Should print: olleh
print(max_of_two(10, 20)) # Should print: 20

def greet_formally(name, pronoun = "Mr."):
    """Returns a formal greeting message."""
    return f"Good day, {pronoun} {name}."

print(greet_formally("Smith")) # Should print: Good day, Mr. Smith.
print(greet_formally("Smith", "Dr.")) # Should print: Good day, Dr. Smith.
print(greet_formally(name="Johnson", pronoun="Ms.")) # Should print: Good day, Ms. Johnson.

def calculate_area(length, width, /): # Positional-only parameters
    """Returns the area of a rectangle."""
    return length * width

print(calculate_area(5, 10)) # Should print: 50
# print(calculate_area(length=5, width=10)) # This will raise a TypeError

def concatenate_strings(*args):
    """Concatenates multiple strings into one."""
    return ' '.join(args)

print(concatenate_strings("Hello", "world!", "How", "are", "you?")) # Should print: Hello world! How are you?

def build_profile(first, last, **user_info): #  Keyword-only parameters
    """Builds a user profile dictionary."""
    profile = {'first_name': first, 'last_name': last}
    profile.update(user_info)
    return profile

user_profile = build_profile('John', 'Doe', location='New York', age=30) # Should print: {'first_name': 'John', 'last_name': 'Doe', 'location': 'New York', 'age': 30}
print(user_profile) 

def my_function(a, b, /, *, c, d): # Positional-only and Keyword-only parameters
  """Returns the sum of four numbers."""
  return a + b + c + d

result = my_function(5, 10, c = 15, d = 20)
print(result) # Should print: 50

# The *args parameter allows a function to accept any number of positional arguments.
def multiply_all(*args):
    """Returns the product of all given numbers."""
    product = 1
    for num in args:
        product *= num
    return product

print(multiply_all(1, 2, 3, 4)) # Should print: 24

"""
The **kwargs parameter allows a function to accept any number of keyword arguments.

Inside the function, kwargs becomes a dictionary containing all the keyword arguments:
"""

def my_function(**myvar):
  print("Type:", type(myvar))
  print("Name:", myvar["name"])
  print("Age:", myvar["age"])
  print("All data:", myvar)

my_function(name = "Tobias", age = 30, city = "Bergen")

def my_function(title, *args, **kwargs): # Combining *args and **kwargs
  print("Title:", title)
  print("Positional arguments:", args)
  print("Keyword arguments:", kwargs)

my_function("User Info", "Emil", "Tobias", age = 25, city = "Oslo")

def my_function(a, b, c):
  return a + b + c

# Using * to unpack a list into arguments:
numbers = [1, 2, 3] # A list of numbers
result = my_function(*numbers) # Same as: my_function(1, 2, 3) 
print(result) # Should print: 6 

# Using ** to unpack a dictionary into arguments:
def my_function(fname, lname):
  print("Hello", fname, lname)

person = {"fname": "Emil", "lname": "Refsnes"}
my_function(**person) # Same as: my_function(fname="Emil", lname="Refsnes")

def myfunc():
  global x # Use the global keyword to modify the global variable x
  x = 300

myfunc()

print(x)

# Without the global keyword, y would be local to myfunc
y = 300

def myfunc():
  y = 200
  print(y)

myfunc()

print(y)

"""
As explained in the example above, the variable x is not available outside the function, but it is available for any function inside the function:
"""

def somaNumbers():
  z = 500
  def add():
    print(z + 5)
  add()
  print(z + 10)

somaNumbers()

def outer_function():
   global outer
   outer = 10
   print(outer)

outer_function()
print(outer + 10)

def function2():
   m = 15
   print(m)
   def function3():
      nonlocal m
      m = 25
      print(m)
   function3()
   print(m)

function2()

# Decorators

# Lambda Functions

# Recursion

# Generators