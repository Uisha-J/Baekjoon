n = int(input())
a = list(map(int, input().split()))

if n >= 3:
    a[0] -= 1
    a[-1] -= 1

for i in range(n-3):
    if a[-1] > a[0]:
        a[-1] -= 1
    else:
        a[0] -= 1

print(max(a[0], a[-1]))
