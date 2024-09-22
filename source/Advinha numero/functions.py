from random import randint
import os

def ClearConsole():
	os.system('cls' if os.name == 'nt' else 'clear');

def ShowStartMessage():
	print('####### Adivinhe o número que estou pensando de 1 a 10 #######')
	print('')

def ShowMessageAfterAttempt():
	ClearConsole()
	ShowStartMessage()

def ShowVictoryMessage(tentativa):
		ClearConsole()
		print('')
		print('Parabéns! Você acertou em ', tentativa, ' tentativas')

def ShowAttemptErrorMsg(Tipo):
		ShowMessageAfterAttempt()
		print('')
		print('Chute um número', Tipo) 

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
        		ShowAttemptErrorMsg('maior') if palpite < numero else ShowAttemptErrorMsg('menor');
        		