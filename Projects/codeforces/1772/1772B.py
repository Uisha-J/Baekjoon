n = int(input())

for i in range(n):
    count = 0
    arr = []
    S = False
    arr.append(list(map(int, input().split())))
    arr.append(list(map(int, input().split())))
    for k in range(4):
        if arr[0][0] < arr[0][1] and arr[1][0] < arr[1][1] and arr[0][0] < arr[1][0] and arr[0][1] < arr[1][1]:
            print('YES')
            S = True
            break
        else:
            arr[0][0], arr[0][1], arr[1][1], arr[1][0] = arr[1][0], arr[0][0], arr[0][1], arr[1][1]
    if S == False:
        print('NO')
