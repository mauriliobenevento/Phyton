# Algoritmo078.py
#
# Expressões regulares - procurando texto especifico sem regular expression
#
# By Maurilio Benevento - 10/07/2019

# procurando texto por parte dele, como exemplo: From:
arquivo = open('mbox.rtf')
for linha in arquivo:
    linha = linha.rstrip()
    if linha.find('From:') >= 0:
        print(linha)

# observe que não foi utilizado linha.starswith
