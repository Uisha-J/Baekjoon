a, b = map(int, input().split())
alist = []
blist = []
clist = []

for i in reversed(range(10)):
    if a - 2**i >= 0:
        a -= 2**i
        alist.append(2**i)

for i in reversed(range(10)):
    if b - 2**i >= 0:
        b -= 2**i
        blist.append(2**i)

for i in range(10):
    if 2**i not in alist and 2**i in blist or 2**i in alist and 2**i not in blist:
        clist.append(2**i)

print(sum(clist))
