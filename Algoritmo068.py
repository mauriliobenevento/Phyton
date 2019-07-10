# Algoritmo068.py
#
# Dicionários  - Varrendo o conteúdo para contagem de nomes - simplificando o for
#
# By Maurilio Benevento - 09/07/2019

conta = dict()
# chave   0        1       2         3          4       5         6
nomes=['money', 'casa', 'money', 'dinheiro', 'casa', 'money', 'chinelo']

for i in nomes:
    conta[i] = conta.get(i, 0) + 1
print(conta)