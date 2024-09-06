import os

def ClearConsole():
	os.system('cls' if os.name == 'nt' else 'clear');

def ShowStartMessage():
	print('####### Adivinhe o número que estou pensando de 1 a 10 #######')
	print('')

def ShowMessageAfterAttempt():
	ClearConsole()
	ShowStartMessage()