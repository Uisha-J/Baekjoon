D1, D2, x = map(int, input().split())
D1x = 0
D2x = 0

if D1 > D2:
    D1x = (x/100)
    D2x = (1-(x/100))
else:
    D2x = (x/100)
    D1x = (1-(x/100))

D1 **= -1
D2 **= -1

print(1/(D1x * D1+D2x * D2))
