import sys

# Exibe informações sobre a versão do Python e o sistema operacional
# este exercício ajuda a entender como acessar informações do sistema usando o módulo sys
# e como formatar strings para exibição.
# E também uso de comentários e do print.

print(f"Versão do Python: {sys.version}")
print(f"Plataforma: {sys.platform}")
print(f"Prefixo de instalação: {sys.prefix}")
print(f"Path do módulo: {sys.path}")
print(f"Nome do sistema operacional: {sys.platform}")
print(f"Versão do sistema operacional: {sys.getwindowsversion() if sys.platform == 'win32' else 'N/A'}")
print('Exemplo de print com aspas simples')

print("Prints numa mesma linha", end=','); print("palavra 1", end=','); print("palavra 2", end=','); print("palavra 3")

print("Eu tinha",41,"anos quando fiz este exercício.")