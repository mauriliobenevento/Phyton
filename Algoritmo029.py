# Algoritmo029.py
#
# Procurando o menor valor de uma lista
#
# By Maurilio Benevento - 05/07/2019

menor = None

print('Antes do laço!')

for i in [90, 2, 3, 22, 12, 22, 33, 46, 67, 87, 92, 16]:
    if menor is None:
        menor = i
    elif i < menor:
        menor = i
    print(menor,i)

print('Depois do laço!',menor)