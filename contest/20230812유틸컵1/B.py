yy, mm, dd = map(int, input().split('-'))
cnt = 0

for i in range(int(input())):
    y, m, d = map(int, input().split('-'))

    if y > yy:
        cnt += 1
        continue
    elif y == yy:
        if m > mm:
            cnt += 1
            continue
        elif m == mm:
            if d >= dd:
                cnt += 1
                continue

print(cnt)
