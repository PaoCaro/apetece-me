"""

Defina a função retira_negativos que recebe como argumento uma lista de números inteiros e devolve a lista resultante de retirar todos os números negativos.

"""

def retira_negativos(w: list) -> list:
    return list(filter(lambda a: a >= 0, w))

print(retira_negativos([25,-1,-212,0,1,2,3]))