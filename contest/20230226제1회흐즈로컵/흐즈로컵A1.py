x, y = input().split()
x = int(x)
y = int(y)
if x % 2 == 1 and y % 2 == 1:
    print(x * y - 1)
else:
    print(x * y)