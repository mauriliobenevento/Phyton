# Algoritmo082.py
#
# Extrair da linha uma parte especifica do texto
#
# By Maurilio Benevento - 10/07/2019


import re

hand = open('mbox.rtf')

numlist = list()
for line in hand:
    line = line.rstrip()
    stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)
    if len(stuff) != 1: continue
    num = float(stuff[0])
    numlist.append(num)
print('Maximo: ', max(numlist))
