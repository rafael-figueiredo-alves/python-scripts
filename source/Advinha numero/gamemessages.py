from consolehelpers import ClearConsole

def ShowStartMessage(ValorMaximo):
	print(f'####### Adivinhe o número que estou pensando de 1 a {ValorMaximo} #######')
	print('')

def ShowMessageAfterAttempt(ValorMaximo):
	ClearConsole()
	ShowStartMessage(ValorMaximo)

def ShowVictoryMessage(tentativa):
		ClearConsole()
		print('')
		print('Parabéns! Você acertou em ', tentativa, ' tentativas')

def ShowAttemptErrorMsg(Tipo, ValorMaximo):
		ShowMessageAfterAttempt(ValorMaximo)
		print('')
		print('Chute um número', Tipo) 
		
def ShowGameOverMsg():
	print('')
	print('####### GAME OVER #######')
	input()
	ClearConsole()
