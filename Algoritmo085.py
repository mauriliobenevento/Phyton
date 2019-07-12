# Algoritmo085.py
#
# Usando urllib em python - muito simples e o retorno é igual ao algoritmo anterior.
#
# By Maurilio Benevento - 11/07/2019

import urllib.request, urllib.parse, urllib.error

arquivo = urllib.request.urlopen('http://tneg.com.br/resposta.txt')
for line in arquivo:
    print(line.decode().strip())
