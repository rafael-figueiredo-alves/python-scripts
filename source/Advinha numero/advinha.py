from random import randint

numero = int(randint(1, 10))
palpite = 0
tentativa = 0

print('####### Adivinhe o número que estou pensando de 1 a 10 #######')
print('')

while palpite != numero:

    palpite = int(input('Digite o seu palpite: '))
    tentativa += 1
    if palpite == numero:
        
        print('')
        print('Parabéns! Você acertou em ', tentativa, ' tentativas')
    elif palpite < numero:
        print('')
        print('Chute um número maior') 
    else:
        print('')
        print('Chute um número menor')
        
print('')    
print('####### GAME OVER #######')       