import shared.console

def InputFloat(PromptText):
	print('')
	valorStr = input(PromptText + '\n')
	if(valorStr.capitalize() == 'Q'):
		shared.console.AskToCloseApp()
	valor = float(valorStr.replace(',', '.'))
	return valor