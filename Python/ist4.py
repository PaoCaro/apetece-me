
def num_it(n: int) -> int:
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