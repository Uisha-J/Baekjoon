import sys
input = sys.stdin.readline

n = int(input())
pfsum = [0] * (n-1)
num = list(map(int, input().split()))
pfsum[0] = num[0]
for i in range(1, n-1):
    pfsum[i] = pfsum[i - 1] + num[i]

sum = 0
for i in range(n-1):
    sum += num[-(i+1)] * pfsum[-(i+1)]
print(sum)
