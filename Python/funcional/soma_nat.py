"""

Defina a função soma_nat que recebe como argumento um número natural  n  e devolve a soma de todos os números naturais até  n .

"""

from functools import reduce

def soma_nat(n: int) -> int:
    return reduce(lambda a, b: a + b, range(1, n  + 1))

print(soma_nat(10212))