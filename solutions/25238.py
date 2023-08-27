a, b = map(int, input().split())
if b == 100:
    print(1)
elif (a * (100 - b)) / 100 < 100:
    print(1)
else:
    print(0)
