# Algoritmo046.py
#
# Tratando erro de nome do arquivo a ser aberto
#
# By Maurilio Benevento - 08/07/2019

fname = input('Abrir qual arquivo?: ')
try:
    arq= open(fname)
except:
    print('Arquivo não pode ser aberto:', fname)
    quit()

# caso contrário continua aqui
for line in arq:
    line = line.rstrip() 
    if not line.startswith('Subject:'):
        continue
    print(line)
