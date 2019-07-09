# Algoritmo063.py
#
# Recortando dados da origem de emails do arquivo de texto -> pegando antes do @
#
# By Maurilio Benevento - 08/07/2019



arq = open('mbox.rtf')
for linha in arq:
    linha = linha.rstrip()
    if not linha.startswith('From ') : continue 
    palavra = linha.split()     # quebra cada linha em palavras
    email = palavra[1]          # recorta o primeiro indice, contendo email completo (com @) 
    origem = email.split('@')   # quebra o email, separando 1a parte e 2a parte com @
    print(origem[0])            # mostra a 1a parte - remetente 

