# Algoritmo065.py
#
# Recortando email após o @ para gerar arquivo para importar no antispam
#
# By Maurilio Benevento - 08/07/2019

arq = open('mbox.rtf')

for linha in arq:
    linha = linha.rstrip()
    quebra = linha.split()
    print('Palavra: ',quebra)
    if quebra[0] != 'From':
        print('Ignore')
        continue
    print(quebra[2])

   