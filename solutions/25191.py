N = int(input())
K = input().split()

A = int(K[0])
B = int(K[1])

if ((A // 2) + B) < N:
    print((A//2)+B)
else:
    print(N)