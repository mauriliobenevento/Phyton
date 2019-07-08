# Algoritmo019.py
#
# Quebra dentro do loop para uma saída. Observe que será pedida a entrada de dados
# enquanto for diferente de 'done' o loop continua. Se for 'done' finaliza.
#
# By Maurilio Benevento - 05/07/2019

while True:
    line = input('>')
    if line == 'done':
        break
    print(line)
print('Done!')
