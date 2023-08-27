from itertools import permutations
import sys
input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
k = int(input())
lst = []
ans = []

for i in range(n):
    lst.append(input().rstrip())

temp = list(permutations(lst, k))

for i in temp:
    ans.append(int(''.join(i)))

print(f"{len(set(ans))}")
