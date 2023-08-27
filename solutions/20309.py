n = int(input())
a = list(map(int, input().split()))

for i in range(n):
    if i % 2 == 0:
        if a[i] % 2 != 0:
            continue
        else:
            print('NO')
            exit()
    else:
        if a[i] % 2 == 0:
            continue
        else:
            print('NO')
            exit()

print('YES')
