# Algoritmo059.py
#
# Listas: Preencher uma lista com While parte 2
#
# By Maurilio Benevento - 08/07/2019


numlista = list()

while True:
    entrada = input('Digite um número: ')
    if entrada == 'f': 
        break
    valor = float(entrada)
    numlista.append(valor)
 
media = sum(numlista) / len(numlista)
print('Média: ', media)
