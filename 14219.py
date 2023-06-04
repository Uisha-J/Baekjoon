x, y = map(int, input().split())

if x % 3 == 0 or y % 3 == 0:
    print('YES')
elif x % 3 != 0 and y % 3 != 0:
    print('NO')
