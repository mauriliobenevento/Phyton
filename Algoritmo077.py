# Algoritmo077.py
#
# As 10 palavras mais comum
#
# By Maurilio Benevento - 10/07/2019


arquivo = open('clown.rtf')
dic = dict()

for lin in arquivo:
    palavras = lin.split()    
    for palavra in palavras:
        dic[palavra] = dic.get(palavra, 0) + 1


lista = list()
for chave, valor in dic.items():
    newtup = (valor,chave)
    lista.append(newtup)

lista = sorted(lista, reverse=True)

for valor, chave in lista[:10]:
    print(chave,valor)
