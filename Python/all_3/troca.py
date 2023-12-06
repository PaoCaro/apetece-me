"""

Considere o seguinte algoritmo para ordenação de listas. 
Dada uma lista  w , encontrar os dois primeiros elementos consecutivos de  w  que não estão ordenados e trocá-los. 
Repetir este procedimento até a lista ficar ordenada (este algoritmo é uma variante do algoritmo de ordenação bubblesort). 
Defina uma função troca que implemente este algoritmo de ordenação sobre listas de inteiros.

"""

import time

def faz(w: list):
    j = 0
    for k in range(1, len(w)):
        if w[k - 1] > w[k]:
            copia = w[k - 1]
            w[k - 1] = w[k]
            w[k] = copia
            print(w)
            j += 1
            time.sleep(2)
    return w, j

def troca(w: list) -> list:

    while faz(w)[1] != 0:
        faz(w)[1]

    print("\n")
    return w


print(troca([9,8,7,2,5,6,8,0]))


"""

if w[k - 1] > w[k]:
    h = w[k - 1]
    w[k - 1] = w[k]
    w[k] = h

1ª ronda:
1430 
1340 
1304 
2ª ronda:
1034 
0134 (já ordenada)

01
12
23
34
45
56
67
78
[...]

"""