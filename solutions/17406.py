def rotate(arr):
    n = len(arr)
    rotated_arr = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            rotated_arr[j][n - i - 1] = arr[i][j]

    return rotated_arr


arr = []
for i in range(3):
    arr.append(list(map(int, input().split())))

print(rotate(arr))
