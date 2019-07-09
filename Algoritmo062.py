# Algoritmo062.py
#
# Recortando dados da origem de emails do arquivo de texto
#
# By Maurilio Benevento - 08/07/2019



arq = open('mbox.rtf')
for linha in arq:
    linha = linha.rstrip()
    if not linha.startswith('From ') : continue 
    palavra = linha.split() # a linha é colocada dentro de uma lista, quebrada por palavras
    print(palavra[2]+' '+palavra[1]) # recortando dia da semana e email 
