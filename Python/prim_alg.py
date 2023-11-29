# Defina a função prim_alg que recebe como argumento um número natural e devolve o primeiro algarismo (o mais significativo) na representação decimal de  n .

def prim_alg(n: str):
    algarismos = range(0, len(n) + 1)
    for i in algarismos:
        neg = ['0','.',',']
        if n[i] not in neg: # 0,02 || 0.123
            print(n[i])
            return


prim_alg(input("escolhe um número: "))