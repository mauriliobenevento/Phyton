# Algoritmo041.py
#
# Procurar caractere dentro da string e recuperar parte da string
#
# By Maurilio Benevento - 08/07/2019

a = 'De: maurilio.benevento@tneg.com.br Segunda, 08/07/2019 12:12:00'

busca = a.find('@') # em qual posição está o caractere
print(busca) # retorna a posição

b = a.find(' ',busca) # qual a posição de um espaço vazio após @
print(b)

c = a[busca+1 : b] # recupera e mostra somente o que está entre posição 1 e 2
print(c)
