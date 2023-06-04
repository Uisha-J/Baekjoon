rows = 100
cols = 100
arr = [[0 for i in range(cols)]for j in range(rows)]

n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    for i in range(10):
        for j in range(10):
            arr[y - i][x + j] = 1

count = 0
for i in range(100):
    count += arr[i].count(1)
print(count)
