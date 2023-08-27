arr = input()

if len(arr) == 1:
    print(0)
    exit()

if arr[0] == arr[-1] == '0':
    arr = arr.split('0')
else:
    arr = arr.split('1')

c = 0

for i in arr:
    if i == '':
        continue
    else:
        c += 1

print(c)
