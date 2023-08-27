lst = []
ans = []
for i in range(int(input())):
    a = input()
    lst.append(a[0])

lst.sort()

ct = 0
for i in range(len(lst) - 1):
    if lst[i] == lst[i+1]:
        ct += 1
    else:
        ct = 0
    if ct == 4:
        ans.append(lst[i+1])

if len(ans) != 0:
    print(''.join(ans))
else:
    print('PREDAJA')
