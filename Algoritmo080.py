# Algoritmo080.py
#
# Expressões regulares - importando biblioteca regular expression e utilizando re.findall()
#
# By Maurilio Benevento - 10/07/2019


import re

x = 'Os meus 387 números da sorte são 45 e 7 e, as vezes, 0 e 90'
y = re.findall('[0-9]+',x)
print(y)
# retorno todos os números da frase. O sinal de + após [0-9] completa com mais digitos, por exemplo 45 e 90.

y = re.findall('[aeiou]+',x)
print(y)
# Somente careteres string minusculas

y = re.findall('ve*',x)
print(y)
# Somente careteres string minusculas
