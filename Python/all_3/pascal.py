"""

Defina uma função pascal que recebe como argumento um número natural  n  e
devolve a  n -ésima linha do triângulo de Pascal. 
Recorde que os elementos do triângulo de Pascal podem ser definidos pelas relações seguintes, em que  pk,i  denota o elemento na posição  i da linha  k :
pk,0=1 
pk,k=1 
pk,i=pk−1,i−1+pk−1,i 

"""

from math import comb

def pascal(n: int) -> list:
    assert n >= 0, "burro"
    return list(map(lambda k: comb(n, k), range(n + 1)))

    # alternativa:
    resultado = []
    for k in range(n + 1):
        resultado.append(comb(n, k))
    return resultado



print(pascal(-1200))