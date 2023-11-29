"""
Retornar um lista com todos os números primos desde 2 até n, n > 2

"""
def primos(n: int) -> list:
    if n <= 2:
        return []

    final = []
    for i in range(2, n + 1):
        contar = 0
        for j in range(1, n + 1):
            if i % j == 0:
                contar += 1
        if contar == 2:
            final.append(i)
    return final

primos(2005)