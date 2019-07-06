# Algoritmo008.py
#
# Estouro de memória e exceção - este exercício demonstra os cuidados de
# conversão sem estouro de memória, considerando o try e except
# Observe que não seria possível converter Texto em Número, exceto se o conteúdo
# do texto for número. Igual ao conceito do excel em soma. 
#
# By Maurilio Benevento - 05/07/2019

nome = 'Maurilio Benevento'
try:
    NomeToNumero = int(nome)
except:
    NomeToNumero = -1
print('Primeiro',NomeToNumero)

nome = '123456'
try:
    NomeToNumero = int(nome)
except:
    NomeToNumero = -1
print('Segundo',NomeToNumero)
