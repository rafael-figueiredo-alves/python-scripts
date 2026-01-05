class person:
    name = "John"
    age = 36
    country = "Norway"

person1 = person()
print(person1.name)
print(person1.age)

# apagar objeto
del person1
print('Pessoa existe' if person1 is not None else 'Pessoa não existe') # gera erro, pois o objeto foi apagado
