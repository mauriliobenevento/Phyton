# Algoritmo070.py
#
# Contando palavras de um arquivo
#
# By Maurilio Benevento - 09/07/2019

nome = input('Entre com o arquivo: ')
arquivo = open(nome)

contagem = dict() 
for i in arquivo:
    palavra = i.split()
    for b in palavra:
        contagem[b] = contagem.get(b,0) + 1
    
print('Resultado', contagem)
