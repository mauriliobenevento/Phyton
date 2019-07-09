# Algoritmo058.py
#
# Listas: Preencher uma lista com While parte 1
#
# By Maurilio Benevento - 08/07/2019


total = 0 
contador = 0

while True:
    entrada = input('Digite um número: ')
    if entrada == 'f': 
        break
    valor = float(entrada)
    total = total + valor
    contador = contador + 1
media = total / contador
print('Média: ', media)
