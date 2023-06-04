import sys

z = int(sys.stdin.readline())

for i in range(z):
    n, k = map(int, sys.stdin.readline().split())
    chestlist = list(map(int, sys.stdin.readline().split()))
    chestlist.sort()
    if n == 0:
        print(0)
    elif k + 1 < n:
        print(max(sum(chestlist[0:n-k]), max(chestlist)))
    else:
        print(max(chestlist))
