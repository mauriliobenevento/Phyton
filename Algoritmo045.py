# Algoritmo045.py
#
# Abrindo arquivo pela escolha do usuário
#
# By Maurilio Benevento - 08/07/2019

fname = input('Abrir qual arquivo?: ')

arq= open(fname)


for line in arq:
    line = line.rstrip() 
    if not line.startswith('Subject:'):
        continue
    print(line)
