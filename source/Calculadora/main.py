import shared.console
import shared.inputs

resetScreen = True

while 1 == 1:

    if(resetScreen):
        shared.console.ClearConsole()
        shared.console.PrintAppTitle("Calculadora em Python", "1.0")
        resetScreen = False

    first_number = shared.inputs.InputFloat("Digite o primeiro número a calcular ou Q para encerrar o aplicativo")
    if(first_number is None):
        continue

    second_number = shared.inputs.InputFloat("Digite o segundo número a calcular ou Q para encerrar o aplicativo")
    if(second_number is None):
        continue

    operacao = shared.inputs.InputOperador("Digite o sinal da operação desejada (+ - * /) ou Q para encerrar o aplicativo")
    if(operacao is None):
        continue

    shared.console.Calculate(first_number, second_number, operacao)

    if(shared.inputs.InputSair()):
        resetScreen = True
        continue
    else:
        shared.console.CloseApp()