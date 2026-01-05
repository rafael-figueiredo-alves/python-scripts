name = input("Digite seu nome: ")
print(f"Olá, {name}!")

try:
    age = int(input("Digite sua idade: "))
    print(f"Você tem {age} anos.")
except ValueError:
    print("Por favor, insira um número válido para a idade.")

continuaLoop = True
while continuaLoop:
    resposta = input("Deseja continuar? (s/n): ").strip().lower()
    if resposta == 's':
        print("Continuando...")
    elif resposta == 'n':
        print("Encerrando o programa.")
        continuaLoop = False
    else:
        print("Resposta inválida. Por favor, digite 's' para sim ou 'n' para não.")

continuaLoop = True

while continuaLoop:
    numero = input("Digite um número entre 1 e 10: ")
    try:
        numero = int(numero)
        if 1 <= numero <= 10:
            print(f"Você digitou o número {numero}.")
            continuaLoop = False
        else:
            print("Número fora do intervalo. Tente novamente.")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")

print(f"Obrigado, {name}, por usar o programa! O numero final digitado foi {numero}.")