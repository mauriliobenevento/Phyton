# Algoritmo079.py
#
# Expressões regulares - importando biblioteca regular expression - 
#
# By Maurilio Benevento - 10/07/2019


import re

arquivo = open('mbox.rtf')
for linha in arquivo:
    linha = linha.rstrip()
    if re.search('^http', linha):
        print(linha)

# observe que é como se tivesse sido utilizado linha.starswith
