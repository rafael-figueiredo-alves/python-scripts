import os

def CleanConsole():
	os.system('cls' if os.name == 'nt' else 'clear')

def InputFloat(PromptText):
	valorStr = input(PromptText + '\n');
	valor = float(valorStr.replace(',', '.'));
	return valor;

def ShowResult(IMC):
	if(IMC < 18.5):
   	  Resultado = 'abaixo do peso, esqueletinho!';
	elif (IMC >= 18.5 and IMC <= 24.9):
	  Resultado = 'com peso adequado, miserável!';
	elif (IMC >= 25 and IMC <= 29.9):
  	  Resultado = 'sobrepeso, um regiminho ajuda, hein!';
	elif (IMC >= 30 and IMC <= 34.9):
	  Resultado = 'obeso, sinal amarelo!';
	elif (IMC >= 35 and IMC <= 29.9):
  	  Resultado = 'obeso, sinal vermelho, fecha essa boca, OK?'
	else:
  	  Resultado = 'uma baleia com obesidade grau 3, fecha essa boca pelo amor de Deus!';
	return Resultado;

def CalcularIMC(peso, altura):
	return peso / (altura * altura);