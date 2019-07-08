# Algoritmo026.py
#
# Achando a médio com o loop - FOR
#
# By Maurilio Benevento - 05/07/2019

contador = 0
soma = 0

print('Antes do laço!', contador, soma)

for i in [90, 2, 3, 22, 12]:
        contador = contador + 1
        soma = soma + i
        print(contador, soma, i)

print('Depois do laço!', contador, soma, soma/contador)