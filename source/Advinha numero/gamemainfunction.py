from random import randint
from gamemessages import ShowVictoryMessage, ShowAttemptErrorMsg

def GameThread():
	numero = int(randint(1, 10))
	palpite = 0
	tentativa = 0
	while palpite != numero:
    		palpite = int(input('Digite o seu palpite: \n'))
			tentativa += 1
    		if palpite == numero:
        		ShowVictoryMessage(tentativa)
    		else: 
        		ShowAttemptErrorMsg('maior') 
				if palpite < numero else ShowAttemptErrorMsg('menor');
        		