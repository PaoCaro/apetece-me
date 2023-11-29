"""
Suponha que a cada lista de números  𝑤  da forma  [𝑎0,𝑎1,…,𝑎𝑛]  se associa o polinómio  𝑝𝑤(𝑥)=𝑎0+𝑎1𝑥+𝑎2𝑥2+⋯+𝑎𝑛𝑥𝑛 .
Defina imperatindice_vamente em Python uma função prod que dadas duas listas de números u e v devolve a lista r tal que  
𝑝𝑟(𝑥)=𝑝𝑢(𝑥)×𝑝𝑣(𝑥) . 
Por exemplo, prod([3,1,1],[1,2]) deverá resultar na lista [3,7,3,2], 
já que se tem  (3+𝑥+𝑥2)×(1+2𝑥)=3+7𝑥+3𝑥2+2𝑥3 .

Neste exercício não pode usar definições por compreensão nem métodos. 

As únicas operações sobre listas permitidas são: lista vazia ([]), 
acesso aos elementos da lista por posição (lista[posição]), 
seccionamento da lista (lista[posição:posição]), 
comparação com a lista vazia (==[]), 
cálculo do comprimento (len) e concatenação (+).

"""

def prod(u: list, v: list) -> list:

    operacoes = 0
    indice_u = 0
    r = []
    zeros = 0

    while zeros != (len(u) + len(v) - 1):
        r = r + [0]
        zeros += 1

    while operacoes != (len(u) * len(v)):
        indice_v = 0
        while indice_v != len(v):
            r[indice_u + indice_v] += u[indice_u] * v[indice_v]
            indice_v += 1

        indice_u += 1
        operacoes += indice_v
    return r


print(prod([-1,1,12], [1,1]))



"""
SOMA DOS INDICES U E V É DIRETAMENTE PROPORCIONAL AO GRAU DO POLINÓMIO
numero total de operacoes => len(v) * len(u)

len(v) + len(u) = len(r) - 1

31 -> 0
32 -> 1

11 -> 1
12 -> 2

11 -> 2
12 -> 3


[1,2,3] [9,1,0]

19
11
10

29
21
20

39
31
30

00
01
02 X

10
11
12 X

k0
k;len(v) X

"""