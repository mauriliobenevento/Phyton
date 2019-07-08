# Algoritmo023.py
#
# Procurando o maior número da lista
#
# By Maurilio Benevento - 05/07/2019

maior_numero = -1

print('Antes do laço!', maior_numero)

for numeros in [2, 67, 12, 90, 18, 22, 31]:
    if numeros > maior_numero:
        maior_numero = numeros
    print(maior_numero, numeros)

print('Depois do laço!', maior_numero)