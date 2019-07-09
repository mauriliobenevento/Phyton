# Algoritmo061.py
#
# Quebrando palavras espaçadas de uma string - com espaços maiores que um tab
#
# By Maurilio Benevento - 08/07/2019


string = 'Um          dia          eu vou voltar para a minha           cidade'

print('\nString com mais espaço entre as palavras')
quebra = string.split()
print(quebra)
print(len(quebra)) # não é considerado os espaços na quebra com split

print('\nNova string tentantiva de quebra')
line = 'primeiro;segundo;terceiro' # uma nova string
pensando = line.split() # quebra com split
print(pensando)
print(len(pensando)) # observe que ainda continua como 1 string, ou seja, não houve quebra

print('\nQuebrando em lista')
pensando = line.split(';') # quebra com split, agora especificando o caracter de orientação ao invés de espaço
print(pensando)
print(len(pensando)) 
