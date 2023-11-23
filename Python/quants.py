"""

Defina imperativamente em Python uma função quants que dada uma lista  𝑤  
de números positivos e um número alvo  𝑘  não negativo devolve a lista de 
todas as listas de quantidades naturais  [𝑞0,…,𝑞𝚕𝚎𝚗(𝚠)−𝟷] tais que:

∑𝑖=0𝚕𝚎𝚗(𝚠)−𝟷(𝑞𝑖∗𝑤[𝑖]==𝑘)

Nomeadamente, quants([1,2,5],6) deverá ser:
[[6,0,0], [0,3,0], [2,2,0], [4,1,0], [1,0,1]].

Neste exercício não pode usar definições por compreensão nem métodos. 

As únicas operações sobre listas permitidas são: lista vazia ([]), acesso aos elementos da lista por posição (lista[posição])
seccionamento da lista (lista[posição:posição])
cálculo do comprimento (len) e concatenação (+). 
Pode usar range.

"""

# sum_{i = 0}^{len(w) - 1} (q_i * w[i] == k)

def soma(w: list, k: int):
    return

def quants(w: list, k: int) -> list:
    copia = w[:]
    Q = []

    lista_zero = w[:]


    for i in range(len(w)):
        for j in range(len(w)):
            lista_zero[j] = 0

        print(w[i])
        if w[i] == 1:
            lista_zero[i] = k
            Q = Q + lista_zero
        else:
            if w[i] == k:
                lista_zero[i] = 1
                Q = Q + lista_zero 
            else:
                if k % w[i] == 0:
                    # i = 0
                    # w[i] = 3
                    # e = 2
                    # w[e] = 2
                    for e in range(len(w)):
                        if w[e] * w[i] == k:
                            print("olha encontrei mais um")
                            lista_zero[i] = w[e]
                            Q = Q + lista_zero
                else:
                    print("olha n ao sei")
        print(lista_zero)
        print("\n")
    print(Q)

quants([3,1,2,5,3], 6)

"""
A) /
    k / w[i] = q[i] (se k % w[i] == 0)

B) +
    a * w[i] + b * w[i + 1] (...)

    
a * b = k (a e b são número naturais) ==> c > 0

se w[i] == k ==> q[i] == 1
se w[i] != k:
    w[i] > k:
        ímpossivel um número q[i] natural tal que w[i] * q[i] == k
                            exemplo: 15 * q[i] == 10
    w[i] < k:   
        k % w[i] == 0: (2 * q[i] == 4)
            j == k // w[i]
                encontrar um w[l] tal que j * w[l] == k

        k % w[i] != 0: (32 * q[i] == 42)        
            um loop em que:
            um q[i] tal que q[i] * w[i] < k
"""