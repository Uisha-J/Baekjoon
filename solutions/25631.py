input()
a = list(map(int, input().split()))
k = dict()

for i in a:
    k[i] = 0

for i in a:
    k[i] += 1

print(max(k.values()))
