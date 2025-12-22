mydict = {"nome": "Rafael", "idade": 41, "cidade": "São Paulo"}
print(mydict)

mydict = dict(nome="Jailza", idade=48, cidade="São Paulo")
print(mydict)

print(len(mydict))
print(type(mydict))
print(isinstance(mydict, dict))
print(mydict["nome"])
print(mydict.get("idade"))
print(mydict.keys())
print(mydict.values())

x = mydict.items() # tupla de tuplas
print(x)

mydict["idade"] = 49
print(mydict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")

thisdict.update({"year": 2020}) # atualiza o valor da chave 'year'
print(thisdict)

thisdict["color"] = "red"
print(thisdict) # adiciona a nova chave 'color'

thisdict.update({"type": "gasoline"})
print(thisdict) # adiciona a nova chave 'type'

thisdict.pop("model")
print(thisdict) # remove a chave 'model'

thisdict.popitem()
print(thisdict) # remove o último item inserido
del thisdict["brand"]
print(thisdict) # remove a chave 'brand'

thisdict.clear()
print(thisdict) # limpa o dicionário
del thisdict
# print(thisdict) # gera erro, pois o dicionário foi deletado

for x in mydict:
  print(x) # itera sobre as chaves

for x in mydict.values():
  print(x) # itera sobre os valores

for x, y in mydict.items():
  print(x, y) # itera sobre chaves e valores

mydict2 = mydict.copy()
print(mydict2)
print(mydict2 is mydict) # False
mydict2 = dict(mydict)
print(mydict2 is mydict) # False
print(mydict2 is mydict) # False
print(mydict2)

for x in mydict.keys():
    print(x)

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

print(myfamily) # dicionário dentro de outro dicionário NestedDictionaries 
print(myfamily["child2"]["name"]) # acessa o nome do segundo filho
print(myfamily["child3"]["year"]) # acessa o ano do terceiro filho
print(len(myfamily)) # número de filhos no dicionário myfamily

for x, obj in myfamily.items():
  print(x) # itera sobre as chaves dos filhos

  for y in obj:
    print(y + ':', obj[y]) # itera sobre as chaves e valores dos filhos

"""
Method	Description
clear()	Removes all the elements from the dictionary
copy()	Returns a copy of the dictionary
fromkeys()	Returns a dictionary with the specified keys and value
get()	Returns the value of the specified key
items()	Returns a list containing a tuple for each key value pair
keys()	Returns a list containing the dictionary's keys
pop()	Removes the element with the specified key
popitem()	Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	Updates the dictionary with the specified key-value pairs
values()	Returns a list of all the values in the dictionary
"""

teste = dict.fromkeys(["nome", "idade"], "desconhecido") # cria um novo dicionário com as chaves 'nome' e 'idade', e valor 'desconhecido'
print(teste) # {'nome': 'desconhecido', 'idade': 'desconhecido'}

teste2 = dict.fromkeys(range(1, 6), "valor padrão") # cria um novo dicionário com as chaves de 1 a 5, e valor 'valor padrão'
print(teste2) # {1: 'valor padrão', 2: 'valor padrão

teste3 = dict.setdefault(teste, "nome", "Rafael") # retorna o valor da chave 'nome'
print(teste3) # Rafael