n = int(input())
lst = list(map(int, input().split()))
ans = max(lst)

for i in range(n):
    if i == 0:
        cur = lst[i]
    else:
        if cur < 0:
            cur = 0
        cur += lst[i]
        ans = max(cur, ans)
print(ans)
