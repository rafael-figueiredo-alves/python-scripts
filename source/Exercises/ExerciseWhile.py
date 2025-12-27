iterador = 1

while iterador <= 10:
    print("O valor de iterador é:", iterador)
    iterador += 1
else:
    print("O laço while foi finalizado.")

countdown = 10
while countdown > 0:
    print("Contagem regressiva:", countdown)
    countdown -= 1
else:
    print("Decolar!")

number = 1
while number <= 5:
    if( number % 2 == 0 ):
        print("Número par:", number)
    print("Número atual:", number)
    number += 1

numero = 1
while numero <= 20:
    if( numero % 3 == 0 ):
        numero += 1
        continue
    print("Número não divisível por 3:", numero)
    numero += 1

n = 1
while n <= 5:
    print("Número atual:", n)
    if n == 3:
        print("Número 3 encontrado, saindo do laço.")
        break
    n += 1
else:
    print("Laço concluído sem interrupção.")