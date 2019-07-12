# Algoritmo086.py
#
# Usando urllib em python - para ler webpage
#
# By Maurilio Benevento - 11/07/2019

import urllib.request, urllib.parse, urllib.error

arquivo = urllib.request.urlopen('http://www.tneg.com.br/index.php')
for line in arquivo:
    print(line.decode().strip())
