# Algoritmo087.py
#
# Json
#
# By Maurilio Benevento - 11/07/2019

import json
data = '''{
    "name"  : "Maurilio",
    "phone" : {
            "type" : "intl", 
            "number": "+55 11997802001"
            },
    "email" : {
            "hide" : "yes"
            }
    }'''

info = json.loads(data)
print('Nome: ',info["name"])
print('Hide: ',info["email"]["hide"])

