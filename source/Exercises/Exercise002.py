import random

print("Here is a random number between 1 and 100:")
print(random.randint(1, 100))

print("Executando casting:")
print(int(3.14))      # Converte float para int
print(float(10))      # Converte int para float
print(str(123))       # Converte int para str
print(bool(0))        # Converte int para bool (0 é False) 
print(bool(42))       # Converte int para bool (qualquer valor diferente de 0 é True)
print(list("hello"))  # Converte str para lista
print(tuple([1, 2, 3])) # Converte lista para tupla
print(set([1, 2, 2, 3])) # Converte lista para set (remove duplicatas)
print(dict([('a', 1), ('b', 2)])) # Converte lista de tuplas para dicionário
print("Casting concluído.")