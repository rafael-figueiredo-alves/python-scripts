resultadoOperacao = None

def verificaResultado():
    if resultadoOperacao is None:
        return "Nenhum resultado disponível."
    else:
        return f"O resultado da operação é: {resultadoOperacao}"

print(verificaResultado())

def realizarOperacao(a, b):
    global resultadoOperacao
    try:
        resultadoOperacao = a / b
    except ZeroDivisionError:
        resultadoOperacao = None
        print("Erro: Divisão por zero não é permitida.")

print(realizarOperacao(10, 0))
print(verificaResultado())
print(realizarOperacao(10, 2))
print(verificaResultado())

def semResultado():
    x  = 10

print(semResultado())  # Isso imprimirá 'None' porque a função não retorna nada
print(type(semResultado()))  # Isso imprimirá <class 'NoneType'>