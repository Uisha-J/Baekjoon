arrlen = int(input())
arr = str(input())

for i in range(1, len(arr)+2):
    left = arr[:i]
    right = arr[-i:]
    counter = 0
    for k in range(len(left)):
        if left[k] != right[k]:
            counter += 1
    if counter == 1:
        print('YES')
        exit()
print('NO')
