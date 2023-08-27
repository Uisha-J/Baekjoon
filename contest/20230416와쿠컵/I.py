n = int(input())
arr = list(input())
gochu = 0
arrscore = 0

gochu = arr.count('G')

for i in range(n):
    if arr[i] == '(':
        arrscore += 1
    elif arr[i] == ')':
        arrscore -= 1

if arrscore >= 0:
    left = (gochu - abs(arrscore)) // 2
    right = gochu - left
if arrscore < 0:
    right = (gochu - abs(arrscore)) // 2
    left = gochu - right

arr = ''.join(arr)
arr = arr.replace('G', '(', left)
arr = arr.replace('G', ')', right)

print(''.join(arr))
