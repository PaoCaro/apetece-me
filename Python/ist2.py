#2. Defina a função div que recebe como argumentos dois números naturais  m  e  n  e devolve o resultado da divisão inteira de  m  por  n . Neste exercício não pode recorrer às operações aritméticas de multiplicação, divisão e resto da divisão inteira.

def div (m: int, n: int) -> int:
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