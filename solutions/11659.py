import sys
input = sys.stdin.readline

N, M = map(int, input().split())
num = list(map(int, input().split()))

for i in range(N-1):
    num[i+1] = num[i] + num[i+1]

for i in range(M):
    a, b = map(int, input().split())
    if a == 1:
        print(num[b-1])
    else:
        print(num[b-1] - num[a-2])
