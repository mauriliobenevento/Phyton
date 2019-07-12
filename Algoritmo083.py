# Algoritmo083.py
#
# Pulando caracter utilizando o prefixo '\ e outros'
#
# By Maurilio Benevento - 10/07/2019


import re

e = 'Uma festa de casamento é consirada na faixa de R$11.323,23 para 5 pessoas'

y = re.findall('\$[0-9.,]+',e)    
print(y)
# retorna somente o valor
