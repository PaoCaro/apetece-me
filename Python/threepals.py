"""

Sabe-se que para todo o número inteiro positivo  𝑛  existem inteiros não-negativos  𝑖,𝑗,𝑘  
que são palíndromos (na habitual notação decimal) tais que 𝑛=𝑖+𝑗+𝑘 . 
Por exemplo, tem-se  31415926 = 31400413 + 15251 + 262
Defina imperativamente em  𝑃𝑦𝑡ℎ𝑜𝑛  uma função threepals que dado um número inteiro positivo n 
devolva um triplo de palíndromos (i,j,k) cuja soma seja n. 

Pode usar, sem a definir, uma função auxiliar palQ que dado um número natural devolve True se se tratar de um palíndromo, e False caso contrário

"""

def soma(w: list, n: int) -> list:
    final = []
    h = 1
    while h < len(w) - 1:
        for i in w:
            for j in w[h:]:
                for k in w[h + 1:]:
                    if i + j + k == n:
                        final.append((i, j, k))
            h += 1
    return final

def threepals(n: int) -> list:
    if n < 0:
        return [()]
    
    total = range(11, n + 1)
    palindromos = []

    for i in total:
        k = 0
        for j in str(i):
            if str(i)[k] == str(i)[len(str(i)) - k - 1]:
                k += 1
            else:
                break
            if k > len(str(i)) // 2:
                palindromos.append(i)
                break
    return soma(palindromos, n)

threepals(31415926)