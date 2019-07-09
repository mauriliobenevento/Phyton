# Algoritmo060.py
#
# Quebrando palavras espaçadas de uma string 
# Após a quebra é gerado um indice como na lista
# - aqui começa um pouco sobre DS e sentimental analysis
#
# By Maurilio Benevento - 08/07/2019


string = 'Um dia eu vou voltar para a minha cidade'

quebra = string.split()
print(quebra)
print(len(quebra))

print('\nAgora no laço')

for i in quebra:
    print(i)
