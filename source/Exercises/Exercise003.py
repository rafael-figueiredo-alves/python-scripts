print("Demo de strings em Python:")

print("Verificando se uma string contém outra string:")
main_string = "Olá, bem-vindo ao mundo de Python!"
substring = "mundo"
if substring in main_string:
    print(f'A substring "{substring}" foi encontrada na string principal.')
else:
    print(f'A substring "{substring}" não foi encontrada na string principal.')
print()
print("Fatiamento de strings:")
sample_string = "Python é divertido"
print("String original:", sample_string)
print("Primeiros 6 caracteres:", sample_string[:6])
print("Caracteres do índice 7 ao 8:", sample_string[7:9])
print("Caracteres do índice 10 até o final:", sample_string[10:])
print("String invertida:", sample_string[::-1])
print("String com índices negativos:", sample_string[-9:-1])
print("String rafael em maiúsculas:", "rafael".upper())
nome = "rafael"
print(f"Nome {nome} capitalizado:", nome.capitalize())
nome = "rafael de figueiredo alves"
print(f"Nome {nome} com cada palavra capitalizada:", nome.title())
nome = "RaFaEl De FiGuEiReDo AlVeS"
print(f"Nome {nome} em minúsculas:", nome.lower())
print(f"Remover espaços em branco inicio e fim: '{'   Olá, Mundo!   '.strip()}'")
print(f"Substituir {sample_string} parte da string:", sample_string.replace("divertido", "incrível"))
Grupo = "maçã, banana, laranja, uva"
print(f"Dividir string {Grupo} em lista:", Grupo.split(", "))
print()