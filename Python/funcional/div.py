"""

Defina a função div que recebe como argumentos dois números naturais  
m  e  n  e devolve o resultado da divisão inteira de  m  por  n . 
Neste exercício não pode recorrer às operações aritméticas de multiplicação, divisão e resto da divisão inteira.

"""

def div(m: int, n: int) -> int:
    if m < n:
        return 0
    
    rep = [ i for i in range(n, m + 1, n) ]
    resultado = list(filter(lambda a: a <= m, rep))
        # EQUIVALENTE: resultado = [ i for i in rep if i <= m ]
    return len(resultado)

print(div(100, 50))
