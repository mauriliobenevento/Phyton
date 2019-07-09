# Algoritmo051.py
#
# Listas: Mostrar o conteúdo da lista utilizando RANGE e LEN
#
# By Maurilio Benevento - 08/07/2019

# lista amigos
# ÍNDICE     0       1         2         3         4          5
amigos = ['João', 'Ventura', 'Tuca', 'Lilian', 'Joaquim', 'Mariana']

print('\n\nPrimeiro loop')
for migo in amigos:
    print('Feliz natal:', migo)

print('\n\nSegundo loop - com range e len')
for migo in range(len(amigos)):
    migo = amigos[migo]
    print('Feliz natal:', migo)

    



