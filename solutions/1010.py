import math
import sys
input = sys.stdin.readline

T = int(input())
for i in range(T):
    P = 1
    N, M = map(int, input().split())
    for i in range(N):
        P *= (M - i)
    P //= math.factorial(N)
    print(P)
