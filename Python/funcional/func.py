from functools import reduce

def fixedpoint(f, x):
    while x != f(x):
        x = f(x)
    return x

def nest(f, n: int, x):
    return reduce(lambda a, b: f(a), range(n), x)