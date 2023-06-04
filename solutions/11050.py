import math


def F(n):
    return math.factorial(n)


N, K = map(int, input().split())

print(F(N)//(F(K)*F((N-K))))
