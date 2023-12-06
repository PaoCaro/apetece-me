from math import inf

#1. Defina a função soma_nat que recebe como argumento um número natural  n  e devolve a soma de todos os números naturais até  n .

def soma_nat (n: int):

    if n < 0:
        print("isso não é um número natural burro de merda")
        return

    total = range(0, n + 1)
    j = 0
    for i in total:
        j += i
    print(j)

soma_nat(int(input("insere um número: ")))

#2. Defina a função div que recebe como argumentos dois números naturais  m  e  n  e devolve o resultado da divisão inteira de  m  por  n . Neste exercício não pode recorrer às operações aritméticas de multiplicação, divisão e resto da divisão inteira.

def div (m: int, n: int):
    # m / n
        if m < 0 and n <= 0:
            return
    
        h = [ n for i in range(0, m) ]

        j = 0
        resultado = 0
        for i in h:  # contar quantas vezes "n" cabe em "m"
            if i + j <= m:
                resultado += 1
            j += n
        print(f'{m}/{n} = {resultado}')
        


m = int(input("m = "))
n = int(input("n = "))
div(m,n)


# Defina a função prim_alg que recebe como argumento um número natural e devolve o primeiro algarismo (o mais significativo) na representação decimal de  n .

def prim_alg(n: str):
    algarismos = range(0, len(n) + 1)
    for i in algarismos:
        neg = ['0','.',',']
        if n[i] not in neg: # 0,02 || 0.123
            print(n[i])
            return


prim_alg(input("escolhe um número: "))


def num_it(n: int):
    if n <= 0:
        print("apenas números naturais")
        return

    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3*n + 1
        print(n)


num_it(int(input("insere um número: ")))



def mapeia(valores: list, f: str):
    funcao = lambda x: eval(f)
    for i in valores:
        print(f'f({int(i)})={funcao(int(i))}')

mapeia(input("escreve ai uns números atoa (separado por espaços): ").split(), input("escreve uma função f(x)="))

def repete(w: list):
    total = [i for i in range(1, len(w))]
    for i in total:
        j = 0
        while j < i: # 0 < 1
            w.insert(i, w[i])
            j += 1
    print(w)

repete(input("escreve qualquer merda(separada por espaços): ").split())


######

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
####


def supremo(w: list):
    if w == []:
        print(-inf)
    else:
        w.sort(reverse = True)
        print(w[0])

supremo([ int(i) for i in input("escreve ai alguns números: ").split() ])