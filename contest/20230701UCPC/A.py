lst = ['N', 'E', 'S', 'W', 'N', 'E', 'S', 'W', 'N', 'E', 'S', 'W', 'N', 'E', 'S', 'W', 'N', 'E', 'S', 'W',
       'N', 'E', 'S', 'W', 'N', 'E', 'S', 'W', 'N', 'E', 'S', 'W', 'N', 'E', 'S', 'W', 'N', 'E', 'S', 'W', ]

p = 12
for i in range(10):
    q = int(input())

    if q == 1:
        p += 1
    elif q == 2:
        p += 2
    else:
        p -= 1

print(lst[p])
