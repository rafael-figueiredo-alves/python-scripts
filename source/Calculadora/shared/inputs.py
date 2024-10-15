import shared.console

def InputFloat(PromptText):
	print('')
	NotClosed = False
	valorStr = input(PromptText + '\n')
	if(valorStr.capitalize() == 'Q'):
		NotClosed = shared.console.AskToCloseApp()
	if(NotClosed == False):
		valor = float(valorStr.replace(',', '.'))
		return valor