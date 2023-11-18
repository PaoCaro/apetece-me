def repete(w: list):
    total = [i for i in range(1, len(w))]
    for i in total:
        j = 0
        while j < i: # 0 < 1
            w.insert(i, w[i])
            j += 1
    print(w)

repete(input("escreve qualquer merda(separada por espaços): ").split())