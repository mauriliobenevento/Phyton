# Algoritmo053.py
#
# Listas: Pegando partes da lista
#
# By Maurilio Benevento - 08/07/2019


# ÍNDICE     0       1         2         3         4          5
amigos = ['João', 'Ventura', 'Tuca', 'Lilian', 'Joaquim', 'Mariana']
colegas =['Miguel', 'José', 'Mixu', 'Patrik']
todos = amigos+colegas # concatenando listas

a=todos[1:3]
b=todos[:4]
c=todos[5:]
d=todos[:]

print(a)
print(b)
print(c)
print(d)
