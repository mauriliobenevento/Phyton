# Algoritmo072.py
#
# Contando palavras mais comuns
#
# By Maurilio Benevento - 09/07/2019

nome = input('Entre com o arquivo: ')
arquivo = open(nome)

dic = dict()
for lin in arquivo  :
    lin = lin.rstrip()
    #print(lin)
    quebra = lin.split()
    #print(quebra)
    for w in quebra:
        dic[w] = dic.get(w,0) + 1
      #  print(w,'new',dic[w])
#print(dic)

# achar as palavras mais comuns
largest = -1
theword = nome
for k,v in dic.items():
    print(k,v)
    if v > largest:
        largest = v
        theword = k
print(theword, largest)

