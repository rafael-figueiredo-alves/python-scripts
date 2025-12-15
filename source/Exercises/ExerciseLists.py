Lista1 = [45, 90, 71, 83, 24, 8, 99, 51]
print("Lista original:", Lista1)
print("Tipo de dato:", type(Lista1))
print("Elemento en la posición 3:", Lista1[3])  # Acceder al cuarto elemento (índice 3)
print("Elemento en la posición 0:", Lista1[0])  # Acceder al primer elemento (índice 0)
print("Elemento na última posição:", Lista1[-1])  # Acceder al último elemento (índice -1)
print("Número na penúltima posição:", Lista1[-2])  # Acceder al penúltimo elemento (índice -2)
print("Sublista de la posición 2 a la 5:", Lista1[2:6])  # Sublista desde el índice 2 hasta el 5
print("Sublista desde el inicio hasta la posición 4:", Lista1[:5])  # Sublista desde el inicio hasta el índice 4
print("Sublista desde la posición 3 hasta el final:", Lista1[3:])  # Sublista desde el índice 3 hasta el final
print("Sublista completa:", Lista1[:])  # Sublista completa
print("Elementos en posiciones pares:", Lista1[::2])  # Elementos en posiciones pares
print("Elementos en posiciones impares:", Lista1[1::2])  # Elementos en posiciones impares
print("Lista invertida:", Lista1[::-1])  # Lista invertida
print("Elementos desde la posición 1 hasta la 6 con paso 2:", Lista1[1:7:2])  # Elementos desde el índice 1 hasta el 6 con paso 2
print("Elementos desde la posición 0 hasta la 5 con paso 3:", Lista1[0:6:3])  # Elementos desde el índice 0 hasta el 5 con paso 3
print("Elementos desde la posición 2 hasta el final con paso 4:", Lista1[2::4])  # Elementos desde el índice 2 hasta el final con paso 4
print("Indices negativos:", Lista1[-7:-2])  # Sublista usando índices negativos


Lista2 = list(("Manzana", "Banana", "Cereza")) # Crear una lista usando el constructor list()
print("Lista 2:", Lista2)
print("Tipo de dato:", type(Lista2))
if("Banana" in Lista2):
    print("La Banana está en la lista.") # Verificar si "Banana" está en la lista
else:
    print("La Banana no está en la lista.")
Lista2[1] = "Naranja"  # Cambiar el segundo elemento a "Naranja"
print("Lista 2 después del cambio:", Lista2)

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"] # Reemplazar un rango con más elementos
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"] # Reemplazar un rango con menos elementos
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon") # Insertar un elemento en la posición 2
print(thislist)
thislist.append("orange") # Agregar un elemento al final de la lista
print(thislist)

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical) # Extender la lista con otra lista
print(thislist)

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple) # Extender la lista con una tupla
print(thislist)

thislist.remove("banana") # Eliminar un elemento por valor
print(thislist)

"""If there are more than one item with the specified value, the remove() method removes the first occurrence:"""

thislist = ["apple", "banana", "cherry", "banana"]
thislist.remove("banana")   # Eliminar la primera ocurrencia de "banana"
print(thislist)

thislist.pop()  # Eliminar el último elemento
print(thislist)
thislist.pop(1)  # Eliminar el elemento en la posición 1
print(thislist)

# outro jeito é com del

thislist = ["apple", "banana", "cherry"]
del thislist[0]  # Eliminar el elemento en la posición 0
print(thislist)

thislist = ["apple", "banana", "cherry"]
del thislist  # Eliminar la lista completa
# print(thislist)  # Esto causará un error porque la lista ya no existe

thislist = ["apple", "banana", "cherry"]
thislist.clear()  # Vaciar la lista
print(thislist)

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x) # Iterar sobre los elementos de la lista

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])  # Iterar usando índices

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1   # Iterar usando un bucle while

thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist] # Usar una lista por comprensión para iterar

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

# Usando list comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]   # Crear una nueva lista con elementos que contienen "a"
print(newlist)

[print(x) for x in fruits if "a" in x]  # Usar lista por comprensión con condición para imprimir elementos

# newlist = [expression for item in iterable if condition == True]

newlist = [x for x in range(10) if x < 5]
print(newlist)  # Crear una nueva lista con números menores a 5

newlist = [x.upper() for x in fruits] # Crear una nueva lista con los elementos en mayúsculas
print(newlist)

newlist = ['hello' for x in fruits]
print(newlist)  # Crear una nueva lista con la palabra "hello" repetida

newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)  # Reemplazar "banana" con "orange" en la nueva lista

newlist.sort()  # Ordenar la lista en orden ascendente
print(newlist)

newlist.sort(reverse=True)  # Ordenar la lista en orden descendente
print(newlist)

def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)  # Ordenar la lista usando una función personalizada como clave

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist) # Ordenar la lista teniendo en cuenta mayúsculas y minúsculas

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist) # Ordenar la lista ignorando mayúsculas y minúsculas

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist) # Invertir el orden de la lista
""" You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2."""

thislist2 = thislist.copy()  # Hacer una copia de la lista
thislist2.append("orange")
print(thislist2)
print(thislist)  # Verificar que la lista original no ha cambiado

# outro jeito de copiar uma lista é com o método list()

thislist3 = list(thislist)  # Hacer una copia de la lista usando el constructor list()
thislist3.append("grape")
print(thislist3)

# You can also make a copy of a list by using the : (slice) operator.

thislist4 = thislist[:]  # Hacer una copia de la lista usando el operador de corte
thislist4.append("melon")
print(thislist4)

# Unir dos listas usando el operador +
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)

"""
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list
"""

print(thislist4.index("banana")) # Devuelve el índice del primer elemento con el valor "banana"
print(thislist4.count("cherry")) # Devuelve el número de elementos con el valor "cherry"