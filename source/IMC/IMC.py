import os

os.system('cls' if os.name == 'nt' else 'clear')

print('########################################################');
print('                 CALCULADORA DE IMC                     ');
print('########################################################');
print('');
pesostr = input('Qual é o seu peso?');
peso = float(pesostr.replace(',', '.'));
print('');
alturastr = input('Qual é a sua altura?');
altura = float(alturastr.replace(',', '.'));
IMC = peso / (altura * altura);
print('');
Resultado = '';
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

print('Você está ', Resultado);

fim = input('\nAperte qualquer tecla para fechar o app')

os.system('cls' if os.name == 'nt' else 'clear')
