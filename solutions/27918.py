import sys
input = sys.stdin.readline

d = 0
p = 0
dstreak = 0
pstreak = 0

for i in range(int(input())):
    win = input().rstrip()
    if win == 'D':
        d += 1
    elif win == 'P':
        p += 1
    if p == (d + 2) or d == (p + 2):
        break

print(str(d) + ':' + str(p))
