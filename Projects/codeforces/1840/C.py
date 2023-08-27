import math
import sys
input = sys.stdin.readline
print = sys.stdout.write


def sum_range(m, n):
    return (n - m + 1) * (m + n) // 2


for i in range(int(input())):
    n, m, k = map(int, input().split())
    date = list(map(int, input().split()))
    score = 0
    available = []
    for j in date:
        if j <= k:
            available.append('O')
        else:
            available.append('X')
    available = (''.join(available)).split('X')
    for k in available:
        if len(k) < m:
            continue
        else:
            score += sum_range(1, len(k) - m + 1)
    print(str(score) + '\n')
