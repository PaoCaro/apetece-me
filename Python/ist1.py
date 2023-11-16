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