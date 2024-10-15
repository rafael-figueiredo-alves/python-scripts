import shared.console
import shared.inputs

shared.console.ClearConsole()
shared.console.PrintAppTitle("Calculadora em Python", "1.0")

while 1 == 1:
    first_number = shared.inputs.InputFloat("Digite o primeiro número a calcular ou Q para encerrar o aplicativo")
    second_number = shared.inputs.InputFloat("Digite o segundo número a calcular ou Q para encerrar o aplicativo")
    operacao = shared.inputs.InputFloat("Digite o sinal da operação desejada (+ - * /) ou Q para encerrar o aplicativo")
    