# Algoritmo069.py
#
# Contando padrões  - palavras
#
# By Maurilio Benevento - 09/07/2019

contagem = dict() 
print('Entre com uma linha de texto: ')
linha = input('')

palavra = linha.split()
print('palavra: ', palavra)

print('Contagem...' )
for i in palavra:
    contagem[i] = contagem.get(i,0) + 1
print('Conta', contagem)
