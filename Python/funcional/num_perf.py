"""

Defina a função num_perf que recebe como argumento um número inteiro positivo e devolve True se esse número for um número perfeito e False em caso contrário. 
Recorde que um número perfeito é um número natural que é igual à soma de todos os seus divisores próprios, isto é, a soma de todos os divisores excluindo o próprio número. 
Pode se assim o entender, definir funções auxiliares, desde que definidas no paradigma funcional.

"""
from functools import reduce

def num_perf(n: int) -> bool:
    div = [ x for x in range(1, n) if n % x == 0 ]
    if reduce(lambda a, b: a + b, div) == n:
        return True
    return False

print(num_perf(5))