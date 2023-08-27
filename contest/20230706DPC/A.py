ans = [0, 0, 0, 0]

for i in range(int(input())):
    a, b, c = map(int, input().split())
    if a == 1:
        ans[3] += 1
    else:
        if b == 1 or b == 2:
            ans[0] += 1
        elif b == 3:
            ans[1] += 1
        elif b == 4:
            ans[2] += 1

for i in ans:
    print(i)
