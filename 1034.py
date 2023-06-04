y, x = map(int, input().split())
arr = [[0 for j in range(x)] for i in range(y)]
off_amount = []
lighted = 0

for i in range(y):
    arr[i] = list(input())
    if '0' in arr[i]:
        off_amount.append(arr[i].count('0'))
    else:
        lighted += 1

action = int(input())

while sum(off_amount) < action:
    action -= 2

off_amount.sort(reverse=True)
while action > 0:
    action -= off_amount.pop()
    if action < 0:
        break
    lighted += 1

print(lighted)
