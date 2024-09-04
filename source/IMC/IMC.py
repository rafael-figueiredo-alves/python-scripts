import MyFunctions

MyFunctions.CleanConsole()

MyFunctions.ShowLogo();

peso = MyFunctions.InputFloat('Qual é o seu peso?');

print('');
altura = MyFunctions.InputFloat('Qual é a sua altura?');

IMC = MyFunctions.CalcularIMC(peso, altura)

Resultado = '';

Resultado = MyFunctions.ShowResult(IMC);

print(f"Você está {Resultado}");

fim = input('\nAperte qualquer tecla para fechar o app\n')

MyFunctions.CleanConsole()
