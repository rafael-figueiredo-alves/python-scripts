"""
range(start, stop, step)
If the range function is called with only one argument, the argument represents the stop value.


The start argument is optional, and if not provided, it defaults to 0.

range(10) returns a sequence of each number from 0 to 9. (The start argument, 0 is inclusive, and the stop argument, 10 is exclusive).
"""

for numero in range(1, 11, 1):
    print(numero)

for numero in range(1, 11, 2):
    print(numero)

teste = range(0, 5000, 15)
print(teste)
print(len(teste))
print(teste[10]) # Should print 150
print(teste[20]) # Should print 300
print(teste[30]) # Should print 450
print(teste[:40]) # Should print first 40 elements
print(teste[40:80]) # Should print elements from index 40 to 79
print(teste[::10]) # Should print every 10th element
print(teste[::-1]) # Should print the range in reverse order
print(5 in teste) # Should print True
print(6 in teste) # Should print False
print(min(teste)) # Should print 0
print(max(teste)) # Should print 4995
print(sum(teste)) # Should print the sum of all elements in the range
print(list(teste)) # Should print the entire list of numbers in the range
print(tuple(teste)) # Should print the entire tuple of numbers in the range
print(set(teste)) # Should print the entire set of numbers in the range
print(type(teste)) # Should print <class 'range'>
print(isinstance(teste, range)) # Should print True
print(repr(teste)) # Should print range(0, 5000, 15)
print(teste[:-1]) # Should print all elements except the last one
print(teste[-10:]) # Should print the last 10 elements
