class Veiculo:
    @property
    def Modelo(self):
        return self._Modelo
    
    @Modelo.setter
    def Modelo(self, value):
        self._Modelo = value
    
    def Mover(self):
        return "Movendo o veículo"

class Carro(Veiculo):
    pass

class Aviao(Veiculo):
    def Mover(self):
        return "Voando o avião"

class Navio(Veiculo):
    def Mover(self):
        return "Navegando o navio"
    
class Bicicleta(Veiculo):
    def Mover(self):
        return "Pedalando a bicicleta"
    
def TestarPolimorfismo(veiculo):
    print(f"{veiculo.Modelo} -> {veiculo.Mover()}")

# Exemplo de uso
carro = Carro()
carro.Modelo = "Sedan"
aviao = Aviao()
aviao.Modelo = "Jato"
navio = Navio()
navio.Modelo = "Cargueiro"
bicicleta = Bicicleta()
bicicleta.Modelo = "Mountain Bike"
for veiculo in [carro, aviao, navio, bicicleta]:
    TestarPolimorfismo(veiculo)