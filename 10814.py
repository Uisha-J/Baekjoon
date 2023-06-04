import sys
input = sys.stdin.readline

registerlist = []

for i in range(int(input())):
    user = list(input().split()) + [i]
    user[0] = int(user[0])
    registerlist.append(tuple(user))

registerlist.sort(key=lambda x: (x[0], x[2]))

for i in range(len(registerlist)):
    print(*list(registerlist[i][:2]))
