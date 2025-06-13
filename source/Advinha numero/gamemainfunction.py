from random import randint
from gamemessages import ShowVictoryMessage, ShowAttemptErrorMsg

def GameThread(ValorMaximo):
    numero = randint(1, int(ValorMaximo))  # 'int()' não é necessário aqui, 'randint' já retorna um inteiro.
    palpite = 0
    tentativa = 0
    while palpite != numero:
        palpite = int(input('Digite o seu palpite: \n'))
        tentativa += 1
        if palpite == numero:
            ShowVictoryMessage(tentativa)
        else:
            if palpite < numero:
                ShowAttemptErrorMsg('maior', ValorMaximo)
            else:
                ShowAttemptErrorMsg('menor', ValorMaximo)

        		