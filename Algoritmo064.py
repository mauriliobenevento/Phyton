# Algoritmo064.py
#
# Recortando email após o @ para gerar arquivo para importar no antispam
#
# By Maurilio Benevento - 08/07/2019

arq = open('mbox.rtf')
for linha in arq:
    linha = linha.rstrip()
    if not linha.startswith('From ') : continue 
    palavra = linha.split()     # quebra cada linha em palavras
    email = palavra[1]          # recorta o primeiro indice, contendo email completo (com @) 
    origem = email.split('@')   # quebra o email, separando 1a parte e 2a parte com @
    print('*',origem[1])            # mostra a 2a parte - remetente 
