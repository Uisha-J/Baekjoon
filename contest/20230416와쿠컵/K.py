import sys
input = sys.stdin.readline

arr = list(input().split())
score = 0
score += arr.count('[')*8
while '[' in arr:
    arr.remove('[')
    arr.remove(']')
for i in range(len(arr)):
    if arr[i].isdigit() == True:
        score += 8
    else:
        K = arr[i]
        score += 12 + len(K)

print(score)
