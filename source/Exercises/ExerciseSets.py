"""
Set Items
Set items are unordered, unchangeable, and do not allow duplicate values.

Unordered
Unordered means that the items in a set do not have a defined order.

Set items can appear in a different order every time you use them, and cannot be referred to by index or key.

Unchangeable
Set items are unchangeable, meaning that we cannot change the items after the set has been created.
"""

thisset = {"apple", "banana", "cherry", "apple"}

print(thisset) # duplicates will be ignored

print(type(thisset))

thisset = {"apple", "banana", "cherry", True, 1, 2} # True is considered as 1

print(thisset)

thisset = {"apple", "banana", "cherry"}

print(len(thisset)) # number of items
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)

"""
The only way to access items in a set is to loop through the set items using a for loop, or to ask if a specified value is present in a set, by using the in keyword.
"""

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

print("banana" in thisset) # returns True because "banana" is present in the set
print("banana" not in thisset) # returns False because "banana" is present in the set

# Once a set is created, you cannot change its items, but you can add new items.
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)
thisset.update(["mango", "grapes", "orange"]) # orange will not be added again
print(thisset)

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical) # Add/join two sets

print(thisset) 

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist) # Add items from a list to a set

print(thisset)

thisset = {"apple", "banana", "cherry"}
thisset.remove("banana") # raises an error if the item to remove does not exist
print(thisset)

thisset = {"apple", "banana", "cherry"}
thisset.discard("banana") # does not raise an error if the item to remove does not exist
print(thisset)

thisset = {"apple", "banana", "cherry"}
x = thisset.pop() # removes a random item
print(x)
print(thisset) # the set after removing the item
thisset.clear() # removes all items
print(thisset)
del thisset # deletes the set entirely
# print(thisset) # this will raise an error because the set no longer exists

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

"""join two sets and return a new set
There are several ways to join two or more sets in Python.

The union() and update() methods joins all items from both sets.

The intersection() method keeps ONLY the duplicates.

The difference() method keeps the items from the first set that are not in the other set(s).

The symmetric_difference() method keeps all items EXCEPT the duplicates.
"""

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2) # returns a new set
print(set3)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set1.update(set2) # modifies set1
print(set1)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.intersection(set2) # returns a new set
print(set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.intersection_update(set2) # modifies set1
print(set1)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.difference(set2) # returns a new set
print(set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.difference_update(set2) # modifies set1
print(set1)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1 | set2
print(set3) # union

# Note: The  | operator only allows you to join sets with sets, and not with other data types like you can with the  union() method.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 & set2
print(set3) # intersection

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2)

print(set3) # items that are not present in both sets

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 ^ set2
print(set3) # symmetric difference # items that are not present in both sets

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.symmetric_difference_update(set2)

print(set1) # modifies set1 to keep only items not present in both sets

x = frozenset({"apple", "banana", "cherry"}) # immutable set
print(x)
print(type(x))

"""
Frozensets are like sets, but they cannot be changed after they are created.
copy()	 	Returns a shallow copy	
difference()	-	Returns a new frozenset with the difference	
intersection()	&	Returns a new frozenset with the intersection	
isdisjoint()	 	Returns whether two frozensets have an intersection	
issubset()	<= / <	Returns True if this frozenset is a (proper) subset of another	
issuperset()	>= / >	Returns True if this frozenset is a (proper) superset of another	
symmetric_difference()	^	Returns a new frozenset with the symmetric differences	
union()	|	Returns a new frozenset containing the union
"""

"""
sets
add()	 	Adds an element to the set
clear()	 	Removes all the elements from the set
copy()	 	Returns a copy of the set
difference()	-	Returns a set containing the difference between two or more sets
difference_update()	-=	Removes the items in this set that are also included in another, specified set
discard()	 	Remove the specified item
intersection()	&	Returns a set, that is the intersection of two other sets
intersection_update()	&=	Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	 	Returns whether two sets have a intersection or not
issubset()	<=	Returns True if all items of this set is present in another set
 	<	Returns True if all items of this set is present in another, larger set
issuperset()	>=	Returns True if all items of another set is present in this set
 	>	Returns True if all items of another, smaller set is present in this set
pop()	 	Removes an element from the set
remove()	 	Removes the specified element
symmetric_difference()	^	Returns a set with the symmetric differences of two sets
symmetric_difference_update()	^=	Inserts the symmetric differences from this set and another
union()	|	Return a set containing the union of sets
update()	|=	Update the set with the union of this set and others
"""