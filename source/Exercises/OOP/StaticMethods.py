class Operacoes:
    PI = 3.14159

    @staticmethod
    def somar(a, b):
        return a + b
    
    @staticmethod
    def subtrair(a, b):
        return a - b
    
    @staticmethod
    def multiplicar(a, b):
        return a * b
    
    @staticmethod
    def dividir(a, b):
        if b == 0:
            raise ValueError("Divisão por zero não é permitida.")
        return a / b
    
# Exemplo de uso:
print(Operacoes.somar(10, 5))        # Output: 15
print(Operacoes.subtrair(10, 5))     # Output: 5
print(Operacoes.multiplicar(10, 5))  # Output: 50
print(Operacoes.dividir(10, 5))      # Output: 2.0
try:
    print(Operacoes.dividir(10, 0))  # Deve levantar um ValueError
except ValueError as e:
    print(e)  # Output: Divisão por zero não é permitida.
print(Operacoes.somar(-3, 7))        # Output: 4
print(Operacoes.subtrair(0, 5))      # Output: -5
print(Operacoes.multiplicar(-2, -4)) # Output: 8
print(Operacoes.dividir(7, 2))      # Output: 3.

print(Operacoes.PI)                   # Output: 3.14159
