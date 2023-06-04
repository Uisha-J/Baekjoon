n = int(input())

for i in range(n):
    k = int(input())
    num = list(map(int, input().split()))

    if 2 not in num:
        print('1')

    elif num.count(2) % 2 != 0:
        print('-1')

    else:
        counter = 0
        for i in range(len(num)):
            if num[i] == 2:
                counter += 1
                if counter == num.count(2) / 2:
                    print(i+1)
