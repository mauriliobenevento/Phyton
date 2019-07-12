# Algoritmo084.py
#
# Requisitando um HTTP request 
#
# By Maurilio Benevento - 11/07/2019


import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('tneg.com.br', 80))
cmd = 'GET http://tneg.com.br/resposta.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())
mysock.close()

# retorna o conteúdo do arquivo texto: resposta.txt