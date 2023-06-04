a, b, c, d, e, f = map(int, input().split())

for i in range(1999):
    for j in range(1999):
        if a * (i-999) + b * (j-999) == c and d * (i-999) + e * (j-999) == f:
            print(i-999, j-999)
