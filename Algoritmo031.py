# Algoritmo031.py
#
# Strings e looping
#
# By Maurilio Benevento - 08/07/2019


fruta = 'beterraba'
indice = 0

print('Primeiro loop com while')
while indice < len(fruta) :
    letra = fruta[indice]
    print(indice, letra)
    if letra=='a' or letra=='A':
        print('----------------letra a')
    indice = indice + 1

print('Segundo loop com FOR')
for letra in fruta:
    if letra=='a' or letra=='A':
        print(letra)
        
indice = 0 
print('Terceiro loop com FOR')
for letra in fruta:
    if letra=='a' or letra=='A':
        print('indice',indice, 'com a letra a')
        indice = indice +1
    else:
        indice = indice +1
        
        




