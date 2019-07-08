# Algoritmo019.py
#
# Finalizando uma iteração com continue
# tudo que iniciar com # na linha 10 não será impresso e continua
#
# By Maurilio Benevento - 05/07/2019

while True:
    line = input('>')
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print(line)
print('Done!')