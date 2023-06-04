import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
    charge = int(input())
    Q = D = N = P = 0
    while charge >= 25:
        charge -= 25
        Q += 1
    while charge >= 10:
        charge -= 10
        D += 1
    while charge >= 5:
        charge -= 5
        N += 1
    while charge >= 1:
        charge -= 1
        P += 1
    print(Q, D, N, P)
