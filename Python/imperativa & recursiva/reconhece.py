"""

O reconhecimento de padrões consiste em verificar se uma determinada sequência padrão 𝑝 ocorre numa outra sequência  𝑠 . 
Considere que, quer a sequência padrão  𝑝 , quer a sequência  𝑠 , são listas. 
Pretende-se verificar se os elementos da lista  𝑝  ocorrem na lista  𝑠 , pela mesma ordem e consecutivamente. 

Apresentam-se em seguida alguns exemplos:

O padrão  [1,2,3]  ocorre na sequência  [2,1,2,3,4,5] ;
O padrão  [4,3,4]  não ocorre na sequência  [2,1,4,2,3,4,5] ;
O padrão  [5,2,7]  ocorre na sequência  [5,2,7] ;
O padrão  [9,4]  ocorre na sequência  [3,2,4,2,9,4] ;
O padrão  [7,4,3]  ocorre na sequência  [7,4,7,4,3,7,2,7] .

Defina uma função reconhece que recebe como argumento duas listas  𝑝  e  𝑠  e devolve True se o padrão  𝑝  ocorre na sequência  𝑠 , e devolve False em caso contrário.

"""

def reconhece(a: list, b: list) -> bool:
    ok = 0
    for B in b:
        if B == a[ok]:
            ok += 1
            if ok == len(a):
                return True
        else:
            ok = 0
    return False
    
reconhece(input("a: ").split(), input("b: ").split())