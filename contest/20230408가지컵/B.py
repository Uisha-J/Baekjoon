import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
farm = K

for i in range(M):
    t, r = map(int, input().split())
    farm -= r
    if farm < 0:
        print(i+1, '1')
        exit()

print('-1')
