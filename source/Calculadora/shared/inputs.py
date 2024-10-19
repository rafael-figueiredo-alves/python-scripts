import shared.console

def InputFloat(PromptText):
	print('')
	NotClosed = False
	valorStr = input(PromptText + '\n')
	if(valorStr.capitalize() == 'Q'):
		NotClosed = shared.console.AskToCloseApp()
	if(NotClosed == False):
		if(valorStr.replace(',', '').isdigit()):
			valor = float(valorStr.replace(',', '.'))
			return valor
		else:
			print("Valor informado é inválido!")
	
def InputOperador(PromptText):
	print('')
	NotClosed = False
	valorStr = input(PromptText + '\n')
	if(valorStr.capitalize() == 'Q'):
		NotClosed = shared.console.AskToCloseApp()
	if(NotClosed == False):
		if(valorStr in ['+', '-', '*', '/']):
			valor = valorStr
			return valor
		else:
			print("Valor informado é inválido!")

def InputSair():
	print('')
	valor = input('Pressione qualquer tecla para realizar um novo cálculo ou Q para encerrar a aplicação\n')
	if(valor.capitalize() == 'Q'):
		return False
	else:
		return True