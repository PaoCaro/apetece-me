# Diz-se que uma lista tem elemento maioritário se mais de metade dos seus elementos forem iguais. Defina a função maioritario que recebe como argumento uma lista  𝑤  e devolve o elemento maioritário de  𝑤 , caso exista, e o número de ocorrências desse elemento. No caso de a lista não ter elemento maioritário a função não devolve valor.

def maioritario(w: list) -> list:
    algarismos = set(w)
    final = []
    for algarismo in algarismos:
        rep = 0
        for elemento in w:
            if algarismo == elemento:
                rep += 1
        if rep > 1:
            if len(final) < rep:
                final.clear()
                final.append(algarismo)
                final.append(rep)
    if len(final) > 1:
        print(final)
        return final

maioritario(input("escreve ai uns número atoa separados por espaços: ").split())
