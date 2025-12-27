numeroInicial = int(input("Digite o número inicial: "))
numeroFinal = int(input("Digite o número final: "))
for numero in range(numeroInicial, numeroFinal + 1):
    print(numero)
# Exercício: Solicite ao usuário que insira um número inicial e um número final. Em seguida, utilize um loop 'for' para imprimir todos os números inteiros entre esses dois valores, inclusive.

# nested-for

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

for x in [0, 1, 2]:
  pass # O loop 'for' itera sobre a lista, mas não faz nada dentro do loop.

# Exercício: Crie dois loops 'for' aninhados. O loop externo deve iterar sobre uma lista de adjetivos e o loop interno deve iterar sobre uma lista de frutas. Imprima todas as combinações possíveis de adjetivos e frutas.
# Exercício: Crie um loop 'for' que itere sobre uma lista de números e utilize a palavra-chave 'pass' dentro do loop. O loop deve percorrer todos os números, mas não deve executar nenhuma ação dentro do loop.

for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")

for x in range(6):
    if x == 3: continue
    print(x)
else:
    print("Finally finished!")

"""
A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.

With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.
"""

listaDeFrutas = ["maçã", "banana", "cereja"]
for fruta in listaDeFrutas:
    print(fruta)
# Exercício: Crie um loop 'for' que itere sobre uma lista de frutas e imprima cada fruta na lista.

for numero in range(6):
    print(numero)

for contagem in range(10):
    if(contagem % 2 == 0):
       continue # Pula os números pares
    print("Número impar de 1 a 10:", contagem)
    contagem += 1