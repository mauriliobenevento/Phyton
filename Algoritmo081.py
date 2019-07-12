# Algoritmo081.py
#
# Expressões regulares - importando biblioteca regular expression e utilizando re.findall()
#
# By Maurilio Benevento - 10/07/2019


import re

e = 'From stephen.marquard@uct.ac.za Fri,  4 Jan 2008 19:49:51 +0000 (GMT)'

y = re.findall('\S+@\S+', e)    
print(y)
# retorna somente o email da variavel e. 

y = re.findall('^From .*@([^ ]*)',e )
print(y)
# Outra forma de extrair considerando a máscara acima.