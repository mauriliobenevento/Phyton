# Algoritmo025.py
#
# Soma e total de uma lista de números com FOR
# a implementação é acumular o conteúdo de i aproveitando o contador
#
# By Maurilio Benevento - 05/07/2019

contador = 0

print('Antes do laço!', contador)

for i in [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 90, 2, 3, 22, 12]:
        contador = contador + i
        print(contador, i)

print('Depois do laço!', contador)