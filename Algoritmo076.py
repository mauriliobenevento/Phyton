# Algoritmo076.py
#
# Classificando com for - invertendo a ordem para Valor e depois Chave
#
# By Maurilio Benevento - 10/07/2019

#    k  v    k  v   k  v   k  v   k  v   k  v 
l ={'a':20, 'b':2, 'c':3, 'h':5, 'd':3, 'f':1}

temp = list()

#aqui está feito a inversão
for k, v in l.items():
    temp.append((v,k))
print(temp,'\n')

# aqui coloca em ordem decrescente pelo valor
temp = sorted(temp, reverse=True)
print(temp)

    