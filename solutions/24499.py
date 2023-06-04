import sys
input = sys.stdin.readline

N, K = map(int, input().split())
applepie = list(map(int, input().split())) * 2
yum = sum(applepie[0:K])
yumlist = []
for i in range(2 * N - K):
    yum = yum - applepie[i] + applepie[K + i]
    yumlist.append(yum)
print(max(yumlist))
