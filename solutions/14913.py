import math

inputlist = list(map(int,input().split()))
a = inputlist[0]
d = inputlist[1]
k = inputlist[2]

if (k - a) % d == 0 and (k - a) / d >= 0:
    print(math.trunc((k - a) / d + 1))
else:
    print('X')