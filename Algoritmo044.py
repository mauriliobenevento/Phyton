# Algoritmo044.py
#
# Procurando string no arquivo
#
# By Maurilio Benevento - 08/07/2019

arq= open('mbox.rtf')

for line in arq:
    line = line.rstrip() 
    if not line.startswith('From:'):
        continue
    print(line)
