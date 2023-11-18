
def soma_f(n: int, d: float, a: int | float, funcao: str) -> float:
    f = lambda x: eval(funcao)
    resultado = 0
    for i in range(1, n + 1):
        resultado += f(a + (i - 1) * d)
    return resultado

def aproximaIntegral(funcao: str, a: float, b: float, n: int):
    if a > b:
        raise TypeError("'a' não pode ser superior a 'b'")
    if n < 0:
        raise TypeError("n < 0 !, não pode")

    """
    já escrevo
    >>> funcao = 9*x + 3
    >>> a = 9
    >>> b = 15
    >>> n = 10000
    >>> aproximaIntegral(funcao, a, b, n)
    k
    """
    d = (b - a) / n
    print(d * soma_f(n, d, a, funcao))
    
aproximaIntegral(input("funcao: "), float(input("a = ")), float(input("b = ")), int(input("n= ")))