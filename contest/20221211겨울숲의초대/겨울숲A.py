N = int(input())
time = 0
house = list(map(int,input().split()))

house.sort(reverse=True)

while N >= 2:

    if house[0]>0 and house[1]>0:
        house[0] -= 1
        house[1] -= 1
        time += 1
        house.sort(reverse=True)
    elif house[0]>=1 and house[1] == 0:
        house[0] -= 1
        time += 1
    else:
        if time > 1440:
            print('-1')
            break
        else:
            print(time)
            break
        

if N == 1 and house[0] < 1441:
    print(house[0])
elif N == 1 and house[0] > 1440:
    print('-1')