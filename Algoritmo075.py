# Algoritmo075.py
#
# Classificando com for
#
# By Maurilio Benevento - 10/07/2019

d ={'a':20, 'b':2, 'c':3, 'h':5, 'd':3, 'f':1}

d.items()
print(sorted(d.items()))
#print(d)

for k, v in sorted(d.items()):
    print(k,v)
    