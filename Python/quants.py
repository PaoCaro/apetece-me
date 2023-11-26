"""

Defina imperativamente em Python uma função quants que dada uma lista  𝑤  
de números positivos e um número alvo  𝑘  não negativo devolve a lista de 
todas as listas de quantidades naturais  [𝑞0,…,𝑞𝚕𝚎𝚗(𝚠)−𝟷] tais que:

∑𝑖=0𝚕𝚎𝚗(𝚠)−𝟷(𝑞𝑖∗𝑤[𝑖]==𝑘)

Nomeadamente, quants([1,2,5], 6) deverá ser:
[[6,0,0], [0,3,0], [2,2,0], [4,1,0], [1,0,1]].

Neste exercício não pode usar definições por compreensão nem métodos. 

As únicas operações sobre listas permitidas são: lista vazia ([]), acesso aos elementos da lista por posição (lista[posição])
seccionamento da lista (lista[posição:posição])
cálculo do comprimento (len) e concatenação (+). 
Pode usar range.

"""

# sum_{i = 0}^{len(w) - 1} (q_i * w[i] == k)

def soma(li: list) -> list:
    menos = 0
    final = []
    for a in range(len(li)):
        for b in range(menos, len(li)):
            final += [li[a] + li[b]]
        menos += 1
    return final

def quants(w: list, k: int) -> list:
    Q = []

    lista_zero = w[:]


    for i in range(len(w)):
        for j in range(len(w)):
            lista_zero[j] = 0

        print(w[i])
        if w[i] == 1:
            lista_zero[i] = k
            Q += lista_zero
        else:
            if w[i] == k:
                lista_zero[i] = 1
                Q += lista_zero 
            else:
                if k % w[i] == 0:
                    # i = 0
                    # w[i] = 3
                    # e = 2
                    # w[e] = 2
                    for e in range(len(w)):
                        if w[e] * w[i] == k: # potências e tabuada-incluida-na-lista
                            print("olha encontrei mais um")
                            lista_zero[i] = w[e]
                            Q += lista_zero
                            break
                    else: # tabuada fora da lista
                        lista_zero[i] = k // w[i]
                        Q += lista_zero



        print(lista_zero)
        print("\n")

    neozero = []
    jota = []
    indices = []
    for i in range(len(w)):
        for j in range(1, k):
            if w[i] * j < k:
                # print(f'{w[i]} * {j} == {w[i] * j}')
                neozero += [w[i] * j]
                jota += [j]
                indices += [w[i]]
    copia = []
    for i in range(len(w) - 1):
        pass



    print("\nindices w[i]: ", indices)
    print("jota: ", jota)
    print("neozero: ", neozero)



quants([1,2,5], 6)
# 2,0 ; 0,4 ; 1,2

# w[i] * q[i]
# a * b < a ou a * b < b
# a e b são naturais

2 * 1 == 2 # A => [1]
# ----- B:
1 * 1 == 1
1 * 2 == 2
1 * 3 == 3

# verificar se é IGUAL a k (AB)
2+1
2+2 # ==> verdadeiro => 1,2 ||  w[i] * q[i]
2+3
#       < k 

# multiplos => range(1,k)

"""
+
++
+++
++++
+++++
k-vezes
"""

"""
SOMA
w = [1,2,5]

sempre < k => menor que k
"""
# A =>      range(1,k)
1 * 1 == 1
1 * 2 == 2
1 * 3 == 3
1 * 4 == 4 
1 * 5 == 5
# ---
# B
2 * 1 == 2
2 * 2 == 4
# ----
# C
5 * 1 == 5

#forma: A + (B,C)
1+2
1+4
1+5
2+2
2+4
2+5
3+2
3+4
3+5
[...]
5+2
5+4
5+5
# agora da forma B + (A,C)
2+1
2+2
2+5


# agora no mínimo uma lista com 2 números:

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
                encontrar um w[e] tal que e * w[l] == k

        k % w[i] != 0: (32 * q[i] == 42)        
            um loop em que:
            um q[i] tal que q[i] * w[i] < k
"""



"""

a b c d
[d, e, f, g, h]
a_ana_é_fish = 0
d + e = o
f + h = x
e + h  = l
x + e = f + h + e



"""

"""

copia[1,2,3,4,5]
neozero[a,b,c,d,e]
copia[i] = copia[i] + neozero[i]
    copia[i] += neozero[i]

"""