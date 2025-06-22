class SomaNumeros:
    Numero1 = int,
    Numero2 = int,
    Resultado = int,

    def __init__(self, num1, num2):
        self.Numero1 = num1
        self.Numero2 = num2
    
    def Somar(self):
        return self.Numero1 + self.Numero2
    

Somando = SomaNumeros(46, 94)

print("A soma de %s e %s é igual a %s" % (Somando.Numero1, Somando.Numero2, Somando.Somar()))

