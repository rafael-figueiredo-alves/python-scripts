from random import randint
from functions import ClearConsole, ShowStartMessage, ShowVictoryMessage, ShowAttemptErrorMsg

ClearConsole();
ShowStartMessage();

numero = int(randint(1, 10))
palpite = 0
tentativa = 0

while palpite != numero:

    palpite = int(input('Digite o seu palpite: \n'))
    tentativa += 1
    if palpite == numero:
        ShowVictoryMessage(tentativa)
    elif palpite < numero:
        ShowAttemptErrorMsg('maior')
    else:
        ShowAttemptErrorMsg('menor')

print('');
print('####### GAME OVER #######');