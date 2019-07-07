# Algoritmo015.py
#
# Retornando valores da função - mais exemplo
#
# By Maurilio Benevento - 05/07/2019


def pais(idioma):
    if idioma == 'es':
        return 'Hola'
    elif idioma == 'fr':
        return 'Bonjour'
    elif idioma == 'br':
        return 'Olá'
    elif idioma == 'en':
        return 'Hello'
    else:
        return 'Hi'

print(pais('es'), 'Mirandez')
print(pais('fr'), 'Carla')
print(pais('br'), 'Guga')
print(pais('en'), 'Bob')
print(pais(''), 'Anyone')

