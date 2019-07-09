# Algoritmo043.py
#
# Procurando string no arquivo
#
# By Maurilio Benevento - 08/07/2019

arq= open('mbox.rtf')

for line in arq:
    if line.startswith('To:'):
        print(line)

# no trecho acima o retorno vem pulando linha

# no trecho abaixo é retirada a linha em branco 
arq1= open('mbox.rtf')

for line in arq1:
    line = line.rstrip() # rstrip retira a linha em branco
    if line.startswith('To:'):
        print(line)
