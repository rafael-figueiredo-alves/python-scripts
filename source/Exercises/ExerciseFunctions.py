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
def decorator_UpperCase(func):
    def inner_wrapper(value):
       return func(value).upper()
    return inner_wrapper

@decorator_UpperCase
def greet_decorated(value):
    return f"Hello, {value}!"

print(greet_decorated("Rafael")) # Should print: HELLO, WORLD!

def log_execution(func):
    def wrapper(*args, **kwargs):
        print(f"Executing function: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} executed successfully.")
        return result
    return wrapper 

@log_execution
def multiply(a, b):
    return a * b

print(multiply(4, 5)) # Should print execution logs and the result: 20

def changecase(value):
   def _Changecase(func):
      def inner_wrapper(name):
         if(value == 0):
          return func(name).upper()
         else: 
          return func(name).lower()
      return inner_wrapper
   return _Changecase

@changecase(0)  
def greet_changecase(name):
   return f"Hello, {name}!"

@changecase(1)  
def greet_changecase2(name):
   return f"Hello, {name}!"

print(greet_changecase("Rafael")) # Should print: HELLO, RAFAEL!
print(greet_changecase2("Rafael")) # Should print: hello, rafael!

"""
when a function is decorated, the metadata of the original function is lost.
To preserve the metadata, use the functools.wraps decorator inside the wrapper function.
"""

def changecase(func):
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Have a great day!"

print(myfunction.__name__) # Should print: myinner

from functools import wraps
def changecase(func):
  @wraps(func)
  def myinner():
    return func().upper()
  return myinner
@changecase
def myfunction():
  return "Have a great day!"

print(myfunction.__name__) # Should print: myfunction

# Lambda Functions
square = lambda x: x * x  # Returns the square of x
print(square(6)) # Should print: 36

somaNumeros = lambda a, b: a + b  # Returns the sum of a and b
print(somaNumeros(10, 15)) # Should print: 25

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))

numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled) # Should print: [2, 4, 6, 8, 10]

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers) # Should print: [1, 3, 5, 7]

words = ["apple", "pie", "banana", "cherry"]
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words) # Should print: ['pie', 'apple', 'banana', 'cherry']

# Recursion
def recursive_factorial(n):
    """Returns the factorial of a number using recursion."""
    print(f"Calculating factorial({n})")
    if n == 0 or n == 1:
        return 1
    else:
        return n * recursive_factorial(n - 1)
    
print(recursive_factorial(5)) # Should print: 120

"""
Every recursive function must have two parts:

A base case - A condition that stops the recursion
A recursive case - The function calling itself with a modified argument
Without a base case, the function would call itself forever, causing a stack overflow error.
"""

def factorial(n):
  # Base case
  if n == 0 or n == 1:
    return 1
  # Recursive case
  else:
    return n * factorial(n - 1)

print(factorial(5))

def sum_list(numbers):
  if len(numbers) == 0:
    return 0
  else:
    return numbers[0] + sum_list(numbers[1:])

my_list = [1, 2, 3, 4, 5]
print(sum_list(my_list)) # Should print: 15

def find_max(numbers):
  if len(numbers) == 1:
    return numbers[0]
  else:
    max_of_rest = find_max(numbers[1:])
    return numbers[0] if numbers[0] > max_of_rest else max_of_rest

my_list = [3, 7, 2, 9, 1]
print(find_max(my_list)) # Should print: 9

import sys
print(sys.getrecursionlimit()) # Default is usually 1000
sys.setrecursionlimit(1500) # Set a new recursion limit
print(sys.getrecursionlimit()) # Should print: 1500

# Increasing the recursion limit should be done with caution. For very deep recursion, consider using iteration instead

# Generators

"""
Generators are functions that can pause and resume their execution.

When a generator function is called, it returns a generator object, which is an iterator.

The code inside the function is not executed yet, it is only compiled. The function only executes when you iterate over the generator.
"""

def my_generator():
  yield 1
  yield 2
  yield 3

for value in my_generator():
  print(value)

def count_up_to(n):
  count = 1
  while count <= n:
    yield count
    count += 1

for num in count_up_to(5):
  print(num)

def large_sequence(n):
  for i in range(n):
    yield i

# This doesn't create a million numbers in memory
gen = large_sequence(1000000)
print(next(gen)) # Should print: 0
print(next(gen)) # Should print: 1
print(next(gen)) # Should print: 2
print(next(gen)) # Should print: 3
print(next(gen)) # Should print: 4
print(next(gen)) # Should print: 5

def simple_gen():
  yield "Emil"
  yield "Tobias"
  yield "Linus"

gen = simple_gen()
print(next(gen))
print(next(gen))
print(next(gen))

# List comprehension - creates a list
list_comp = [x * x for x in range(5)]
print(list_comp)

# Generator expression - creates a generator
gen_exp = (x * x for x in range(5))
print(gen_exp)
print(list(gen_exp))

def echo_generator():
  while True:
    received = yield
    print("Received:", received)

gen = echo_generator()
next(gen) # Prime the generator
gen.send("Hello")
gen.send("World") #   Should print: Received: World

def my_gen():
  try:
    yield 1
    yield 2
    yield 3
  finally:
    print("Generator closed")

gen = my_gen()
print(next(gen)) # Should print: 1
gen.close() # Should print: Generator closed