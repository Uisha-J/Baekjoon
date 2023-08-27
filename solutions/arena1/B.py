m = []
n = []

for i in range(int(input())):
    m.append(input())

for i in range(int(input())):
    n.append(input())

for i in range(len(n)):
    if n[i] in m:
        n[i] = 0

while 0 in n:
    n.remove(0)

if len(m) == 1:
    print(n[0])
    exit()

for i in range(len(m)):
    if m[i] == '?':
        p = m.index('?')
        break

if p == len(m) - 1:  # 맨뒤
    left = m[p-1][-1]
    for i in range(len(n)):
        if n[i][0] == left:
            ans = n[i]

elif p == 0:  # 맨앞
    right = m[p+1][0]
    for i in range(len(n)):
        if n[i][-1] == right:
            ans = n[i]

else:  # 사이
    left = m[p-1][-1]
    right = m[p+1][0]
    for i in range(len(n)):
        if n[i][0] == left and n[i][-1] == right:
            ans = n[i]

print(''.join(ans))
