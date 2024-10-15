import os

def ClearConsole():
	os.system('cls' if os.name == 'nt' else 'clear');

def PrintAppTitle(title, versao):
	print("#####################################################################################################")
	print(f"                               {title} - versão {versao}")
	print("#####################################################################################################")

def AskToCloseApp():
	answer = input('\nDeseja realmente finalizar a aplicação? Digite S para confirmar e N para cancelar ação.\n')
	if(answer.capitalize() == 'S'):
		CloseApp()
	else:
		return True

def CloseApp():
	ClearConsole()
	exit()
	