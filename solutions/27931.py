import sys
input = sys.stdin.readline
debug = print
print = sys.stdout.write

N = int(input())
gaplist = []
arr = list(map(int, input().split()))
oddfound = False
evenfound = False

arr.sort()

for i in range(N-1):
    gap = arr[i + 1] - arr[i]
    gaplist.append(gap)

sortedgaplist = sorted(gaplist)

for i in range(len(gaplist)):
    if sortedgaplist[i] % 2 == 1:
        odd = sortedgaplist[i]
        oddfound = True
        break

for i in range(len(gaplist)):
    if sortedgaplist[i] % 2 == 0:
        even = sortedgaplist[i]
        evenfound = True
        break

for i in range(len(gaplist) - 1):
    if (gaplist[i] + gaplist[i + 1]) % 2 == 0:
        if evenfound == False:
            even = gaplist[i] + gaplist[i + 1]
            evenfound = True
        elif even > gaplist[i] + gaplist[i + 1] and evenfound == True:
            even = gaplist[i] + gaplist[i + 1]

if evenfound == True:
    print(str(even))
else:
    print('-1')

print(' ')

if oddfound == True:
    print(str(odd))
else:
    print('-1')
