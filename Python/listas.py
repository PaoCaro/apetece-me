# 1234
# 2134
# 3214
# 4231

# 1234 # sempre n digitos => len(h) [0,len(h)]

# # em índices
# 0:[1,3] # 1 234
# 1:[[2:3] + 0] # 2 134
# 2:[[0:1] + 3] # 3 123
# 3:[0:2] # 4 123
# ######

#func (nCk) => recursivo (nCk * k!)
# n = 0
# h[len(h) - n]
# n -= 1

# nCk
from math import factorial

def criar(w: list):
    conta = 0
    final = []
    while conta < factorial(len(w)):
        for ra in range(len(w) - 1, 0, -1): #len(h) = 4
            primeiro = w[ra]
            w[ra] = w[0]
            w[0] = primeiro
            conta += 1
    print(conta)
    print(final)
criar([1,2,3])

# 4! 


1342
1423
1234

4231
4123



3241
# ------------
1234
1243
1324
1342
1423
1432
#####
2134
2143
2314
2341
2431
2413
