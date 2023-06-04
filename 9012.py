for i in range(int(input())):
    count = 0
    arr = list(input())
    for j in range(len(arr)):
        if arr[j] == '(':
            count += 1
        else:
            count -= 1
        if count < 0:
            break
    if count == 0:
        print('YES')
    else:
        print('NO')
