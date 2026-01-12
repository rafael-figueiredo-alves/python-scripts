lista_de_numeros = [10, 4, 60, 23, 75, 1, 90]

lista_de_numeros.append(100)  # Adiciona 100 ao final da lista
print("Após append(100):", lista_de_numeros)

lista_de_numeros.insert(2, 50)  # Insere 50 na posição de índice 2
print("Após insert(2, 50):", lista_de_numeros)

lista_de_numeros.remove(23)  # Remove o valor 23 da lista
print("Após remove(23):", lista_de_numeros)

lista_de_numeros.pop()  # Remove o último elemento da lista
print("Após pop():", lista_de_numeros)

lista_de_numeros.sort()  # Ordena a lista em ordem crescente
print("Após sort():", lista_de_numeros)

lista_de_numeros.reverse()  # Inverte a ordem da lista
print("Após reverse():", lista_de_numeros)

index_of_60 = lista_de_numeros.index(60)  # Encontra o índice do valor 60
print("Índice de 60:", index_of_60)

count_of_10 = lista_de_numeros.count(10)  # Conta quantas vezes o valor 10 aparece na lista
print("Contagem de 10:", count_of_10)

sliced_list = lista_de_numeros[2:5]  # Fatiamento da lista do índice 2 ao 4
print("Fatiamento [2:5]:", sliced_list)