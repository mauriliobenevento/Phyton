# Algoritmo071.py
#
# Contando palavras de um arquivo - parte 2
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
        print(w,'new',dic[w])
print(dic)

# abaixo temos uma classificaçào utilizando for
#for k, v in sorted(dic.items()):
#    print(k,v)
    