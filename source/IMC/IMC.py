import MyFunctions

MyFunctions.CleanConsole()

print('########################################################');
print('                 CALCULADORA DE IMC                     ');
print('########################################################');

print('');
peso = MyFunctions.InputFloat('Qual é o seu peso?');

print('');
altura = MyFunctions.InputFloat('Qual é a sua altura?');

IMC = MyFunctions.CalcularIMC(peso, altura)
print('');

Resultado = '';

Resultado = MyFunctions.ShowResult(IMC);

print(f"Você está {Resultado}");

fim = input('\nAperte qualquer tecla para fechar o app\n')

MyFunctions.CleanConsole()
