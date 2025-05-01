from consolehelpers import ClearConsole

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
		
def ShowGameOverMsg():
	print('')
	print('####### GAME OVER #######')
	input()
	ClearConsole()
