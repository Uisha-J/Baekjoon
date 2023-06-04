catastrope = []
n = int(input())

for i in range(666, 2700000):
    arr = list(str(i))
    for k in range(len(arr)-2):
        if arr[k] == arr[k+1] == arr[k+2] == '6':
            catastrope.append(i)
            break
    if len(catastrope) > n:
        break
catastrope.sort()
print(catastrope[n-1])
