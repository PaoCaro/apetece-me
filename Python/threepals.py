"""

Sabe-se que para todo o número inteiro positivo  𝑛  existem inteiros não-negativos  𝑖,𝑗,𝑘  
que são palíndromos (na habitual notação decimal) tais que 𝑛=𝑖+𝑗+𝑘 . 
Por exemplo, tem-se  31415926 = 31400413 + 15251 + 262
Defina imperativamente em  𝑃𝑦𝑡ℎ𝑜𝑛  uma função threepals que dado um número inteiro positivo n 
devolva um triplo de palíndromos (i,j,k) cuja soma seja n. 

Pode usar, sem a definir, uma função auxiliar palQ que dado um número natural devolve True se se tratar de um palíndromo, e False caso contrário

"""

def threepals(n: int) -> tuple:
    if n < 0:
        return ()
    

threepals(31415926)