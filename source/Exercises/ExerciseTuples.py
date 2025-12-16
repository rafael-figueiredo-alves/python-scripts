Mytuple = (1, 2, 3, 5)
print(Mytuple)

print(type(Mytuple))

notatuple = (5)
print(type(notatuple))
print(notatuple)

atuple = (5,)
print(type(atuple))
print(atuple)

emptytuple = ()
print(type(emptytuple))
print(emptytuple)

# Tuple unpacking
a, b, c, d = Mytuple
print(a)
print(b)
print(c)
print(d)


thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5]) # from index 2 to index 5 (not included)

thistuple = ("apple", "banana", "cherry")
print(thistuple[-1]) # last item

thistuple = ("apple", "banana", "cherry")
print(thistuple[1]) # second item

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4]) # from beginning to index 4 (not included)

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:]) # from index 2 to the end

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1]) # from index -4 to index -1 (not included)

thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")

"""
Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.

But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.
"""

tupleX = ("apple", "banana", "cherry")
listY = list(tupleX)
listY[1] = "kiwi"
tupleX = tuple(listY)

print(tupleX)

"""
2. Add tuple to a tuple. You are allowed to add tuples to tuples, so if you want to add one item, (or many), create a new tuple with the item(s), and add it to the existing tuple:
"""

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
tuple3 = tuple1 + tuple2
print(tuple3)

# or

tuple1 = (1, 2, 3)
tuple1 += (4, 5, 6)
print(tuple1)

del tuple1
# print(tuple1) # this will raise an error because the tuple no longer exists

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits # red will get all values that are not assigned to green or yellow

print(green)
print(yellow)
print(red)

fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits # red will get the last value

print(green)
print(yellow)
print(red)

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits # tropic will get all values between green and red

print(green)
print(tropic)
print(red)

thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])

thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i += 1

thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple.count("cherry"))
print(thistuple.count("apple"))
print(thistuple.count("grape"))
print(thistuple.index("orange"))
print(thistuple.index("banana"))
print(thistuple.index("mango"))

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2 # create a new tuple by multiplying

print(mytuple)