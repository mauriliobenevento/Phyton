# Algoritmo042.py
#
# Lendo dados de arquivo txt
#
# By Maurilio Benevento - 08/07/2019

fbox = open('mbox.rtf','r')
print(fbox)

count=0

# uma maneira de mostrar as linhas do arquivo
for arq in fbox:
    count = count+1    
    print('Linha: ',count)

# Tamanho do arquivo 
arq1 = open('mbox.rtf')
linhas = arq1.read()
print(len(linhas))

print(linhas[:20])
