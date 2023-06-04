n, m= input().split()
n = int(n)
m = int(m)
test = list(input() for i in range(n*2))
NotEyfa = False

for _ in range(n):
    arr = test[_]
    for k in range(m):
        arr = list(arr)
        arr[k] = arr[k] * 2
    arr = ''.join(arr)
    if arr != test[_ + n]:
        NotEyfa = True

if NotEyfa == True:
    print('Not Eyfa')
else:
    print('Eyfa')