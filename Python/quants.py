"""

Defina imperativamente em Python uma função quants que dada uma lista  𝑤  
de números positivos e um número alvo  𝑘  não negativo devolve a lista de 
todas as listas de quantidades naturais  [𝑞0,…,𝑞𝚕𝚎𝚗(𝚠)−𝟷] tais que:

∑𝑖=0𝚕𝚎𝚗(𝚠)−𝟷(𝑞𝑖∗𝑤[𝑖]==𝑘)

Nomeadamente, quants([1,2,5],6) deverá ser [[6,0,0], [0,3,0], [2,2,0], [4,1,0], [1,0,1]].

Neste exercício não pode usar definições por compreensão nem métodos. 

As únicas operações sobre listas permitidas são: lista vazia ([]), acesso aos elementos da lista por posição (lista[posição])
seccionamento da lista (lista[posição:posição])
cálculo do comprimento (len) e concatenação (+). 
Pode usar range.

"""

# sum_{i = 0}^{len(w) - 1} (q_i * w[i] == k)

def quants(w: list, k: int) -> list:
    copia = w[:]
    tenta = range(0, k + 1)
    Q = []
    indexes = range(0, len(w))

    for i in indexes:
        for t in tenta:
            copia[i] = t
            print(copia)
"""


"""

quants([1,2,5], 6)