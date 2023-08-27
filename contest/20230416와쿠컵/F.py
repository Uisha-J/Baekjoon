n = int(input())
arr = set(input().split())

counter = 0
for i in range(len(arr)):
    if len(arr[i]) >= 6 and arr[-6:] == 'Cheese:':
        counter += 1

if counter >= 4:
    print('yummy')
else:
    print('sad')
