import sys
input = sys.stdin.readline
print = sys.stdout.write

stick = []

for i in range(int(input())):
    stick.append(int(input()))

for i in range(1, len(stick) + 1):
    if i == 1:
        temp = stick[-i]
        ct = 1
    else:
        if stick[-i] > temp:
            temp = stick[-i]
            ct += 1
        else:
            pass
print(f"{ct}")
