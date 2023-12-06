from math import inf

def supremo(w: list):
    if w == []:
        print(-inf)
    else:
        w.sort(reverse = True)
        print(w[0])

supremo([ int(i) for i in input("escreve ai alguns números: ").split() ])