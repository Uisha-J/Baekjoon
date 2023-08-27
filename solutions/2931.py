y, x = map(int, input().split())

field = []
for i in range(y):
    a = []
    a.append(list(input()))
    if 'M' in a:
        m = (i, a.index('M'))
    if 'Z' in a:
        z = (i, a.index('Z'))

print(field, m, z)
