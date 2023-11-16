def mapeia(valores: list, f: str):
    funcao = lambda x: eval(f)
    for i in valores:
        print(f'f({int(i)})={funcao(int(i))}')

mapeia(input("escreve ai uns números atoa (separado por espaços): ").split(), input("escreve uma função f(x)="))