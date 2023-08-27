import sys
input = sys.stdin.readline
debug = print
print = sys.stdout.write

n = int(input().strip())

for i in range(n):
    size, x1, y1, x2, y2 = map(int, input().strip().split())
    x1 -= size//2
    x2 -= size//2
    y1 -= size//2
    y2 -= size//2
    if x1 > 0:
        x1 = -x1
    else:
        x1 -= 1
    if x2 > 0:
        x2 = -x2
    else:
        x2 -= 1
    if y1 > 0:
        y1 = -y1
    else:
        y1 -= 1
    if y2 > 0:
        y2 = -y2
    else:
        y2 -= 1
    start = max(abs(x1), abs(y1))
    end = max(abs(x2), abs(y2))
    if size == 2:
        print('0\n')
    else:
        print(str(abs(int(start - end))))
        print("\n")
