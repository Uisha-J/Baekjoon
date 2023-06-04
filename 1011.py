import math


def time(x, y):
    dis = y - x
    if dis == 1:
        print('1')
    elif dis == 2:
        print('2')
    elif dis == 3:
        print('3')
    else:
        if dis == int(math.sqrt(dis))**2:
            print(int(math.sqrt(dis))*2 - 1)
        elif dis > int(math.sqrt(dis))**2 + int(math.sqrt(dis)):
            print(int(math.sqrt(dis))*2 + 1)
        elif int(math.sqrt(dis))**2 < dis <= int(math.sqrt(dis))**2 + int(math.sqrt(dis)):
            print(int(math.sqrt(dis))*2)


n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    time(x, y)
