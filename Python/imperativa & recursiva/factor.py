"""

Pelo teorema fundamental da aritmética, todo o número inteiro positivo tem uma factorização única 
como produto de números primos.
Defina imperativamente em Python uma função factor que dado um inteiro positivo  𝚗  
devolva a factorização de  𝚗  na forma de uma lista de pares  
[(𝚙𝟷,𝚎𝟷),...,(𝚙𝚔,𝚎𝚔)]  onde cada  𝚙𝚒  é um número primo e cada  𝚎𝚒  é um inteiro positivo tais que 
 𝚗=𝚙𝚎𝟷𝟷×⋯×𝚙𝚎𝚔𝚔 .

Por exemplo, factor(200) deverá ser [(2, 3), (5, 2)]

"""

import primos

def factor(n: int) -> list:
    if n < 0:
        return []
    
    final = []

    for i in primos(n):
        contar = 0
        pivo = i
        if n % i == 0:
            while n % pivo == 0:
                contar += 1
                pivo *= i
            final.append((i, contar))
    return final

print(factor(2))

"""
contar = 4


200 / 2 até dar float, contar quantas vezes
verificar se dá 200
200 / 3 até dar float
verificar se dá 200
200 / 5 até dar float
verificar se dá 200
se der 200 ==> return

"""