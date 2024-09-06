from random import randint
from functions import ClearConsole, ShowStartMessage, ShowMessageAfterAttempt

ClearConsole();
ShowStartMessage();

numero = int(randint(1, 10))
palpite = 0
tentativa = 0

while palpite != numero:

    palpite = int(input('Digite o seu palpite: '))
    tentativa += 1
    if palpite == numero:
        ClearConsole()
        print('')
        print('Parabéns! Você acertou em ', tentativa, ' tentativas')
    elif palpite < numero:
        ShowMessageAfterAttempt()
        print('')
        print('Chute um número maior') 
    else:
        ShowMessageAfterAttempt()
        print('')
        print('Chute um número menor')

print('');
print('####### GAME OVER #######');