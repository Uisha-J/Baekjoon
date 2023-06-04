import sys
import math
from collections import Counter


def modefinder(numbers):
    c = Counter(numbers)
    global modes
    order = c.most_common()
    maximum = order[0][1]

    modes = []
    for num in order:
        if num[1] == maximum:
            modes.append(num[0])
    return modes


N = int(sys.stdin.readline())
numlist = []

for i in range(N):
    numlist.append(int(sys.stdin.readline()))

numlist.sort()
if len(numlist) == 1:
    numlist_range = 0
else:
    numlist_range = numlist[0] - numlist[-1]

modelist = modefinder(numlist)

if len(modelist) == 1:
    mode_num = modelist[0]
else:
    mode_num = sorted(modelist, reverse=True)[-2]

print(round(sum(numlist)/N))
print(numlist[len(numlist)//2])
print(mode_num)
print(abs(numlist_range))
