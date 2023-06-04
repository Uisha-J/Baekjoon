import itertools

A = input().split()
n = int(A[0])
m = int(A[1])
arr = input().split()
ansarr = []
trashcan = []

result = list(itertools.combinations(arr,3))

for i in range(len(result)):
    k = sum(list(map(int, result[i])))
    if k <= m:
        ansarr.append(k)
    else:
        trashcan.append('0')

maxansarr = max(ansarr)

print(maxansarr)