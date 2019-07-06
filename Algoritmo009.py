# Algoritmo009.py
#
# Uso do try e except em um exemplo real
#
# By Maurilio Benevento - 05/07/2019

senha = input('Entre com a sua senha numérica: ')
try:
    TestaSenhaNumerica = int(senha)
except:
    TestaSenhaNumerica = -1

if TestaSenhaNumerica > 0:
    print('Muito bem, a senha é numérica')
else:
    print('a senha digitada não é numérica')
    