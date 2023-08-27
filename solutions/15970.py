import sys
input = sys.stdin.readline

line = []
colorset = []

for i in range(int(input())):
    a, b = map(int, input().split())
    line.append((a, b))

line.sort(key=lambda x: (x[1], x[0]))
sum = 0

for i in range(len(line)):
    left = False
    right = False
    try:
        if line[i][1] == line[i-1][1]:
            left = abs(line[i][0] - line[i-1][0])
    except:
        pass
    try:
        if line[i][1] == line[i+1][1]:
            right = abs(line[i][0] - line[i+1][0])
    except:
        pass
    if type(left) == int and type(right) == int:
        if left <= right:
            sum += left
        else:
            sum += right
    elif type(left) == int and type(right) == bool:
        sum += left
    elif type(right) == int and type(left) == bool:
        sum += right

print(sum)
