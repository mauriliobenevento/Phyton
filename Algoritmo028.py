# Algoritmo028.py
#
# Procurando números com variáveis booleana (True e False)
#
# By Maurilio Benevento - 05/07/2019

encontrado = False

print('Antes do laço!', encontrado)

for i in [90, 2, 3, 22, 12, 22, 33, 46, 67, 87, 92, 16]:
        if i == 46:
            encontrado = True
        print(encontrado,i)

print('Depois do laço!',encontrado)