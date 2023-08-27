n = int(input())
lst = list(map(int, input().split()))

for i in range(n):
    lvl = lst[i]
    if lvl == 300:
        lst[i] = 1
    elif 275 <= lvl < 300:
        lst[i] = 2
    elif 250 <= lvl < 275:
        lst[i] = 3
    else:
        lst[i] = 4

print(*lst)
