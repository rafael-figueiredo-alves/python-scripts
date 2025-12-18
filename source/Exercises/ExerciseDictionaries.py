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

x = mydict.items()
print(x)

mydict["idade"] = 49
print(mydict)

