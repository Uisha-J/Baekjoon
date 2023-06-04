k = int(input())
arr = list(map(int, input().split()))
count = 1

for i in range(len(arr) - 1):
    if arr[i+1] < arr[i]:
        pass
    else:
        count += 1

print(count)
