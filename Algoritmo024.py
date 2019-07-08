# Algoritmo024.py
#
# Outra forma de loop com for. Contando os laços dentro de uma lista de numeros
#
# By Maurilio Benevento - 05/07/2019

contador = 0

print('Antes do laço!', contador)

for i in [1, 9, 11, 3, 5, 101, 88, 98, 45, 32]:
        contador = contador + 1
        print(contador, i)

print('Depois do laço!', contador)