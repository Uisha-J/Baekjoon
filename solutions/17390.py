import sys
input = sys.stdin.readline
print = sys.stdout.write

n, q = map(int, input().split())
lst = sorted(list(map(int, input().split())))
lst = [0] + lst

for i in range(1, n + 1):
    lst[i] = lst[i] + lst[i-1]

for i in range(q):
    l, r = map(int, input().split())
    print(f"{lst[r] - lst[l - 1]}\n")
