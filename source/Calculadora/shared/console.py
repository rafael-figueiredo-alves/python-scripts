import os

def ClearConsole():
	os.system('cls' if os.name == 'nt' else 'clear');

def PrintAppTitle(title, versao):
	print("#####################################################################################################")
	print(f"{title} - versão {versao}")
	print("#####################################################################################################")
	
def CloseApp():
	input('\nPressione qualquer tecla para fechar o sistema\n')
	ClearConsole()
	