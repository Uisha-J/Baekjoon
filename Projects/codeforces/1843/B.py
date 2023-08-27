import sys
input = sys.stdin.readline
print = sys.stdout.write

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    ans1 = sum(list(map(abs, arr)))

    for i in range(len(arr)):
        if arr[i] > 0:
            arr[i] = 'k'

    for i in range(len(arr)-1):
        if arr[i] == arr[i+1] == 0:
            arr[i] = ''

    arr = map(str, arr)

    arr = ''.join(arr)

    mylist = arr.split('k')

    count = 0
    for i in range(len(mylist)):
        if len(mylist[i]) == 0 or mylist[i] == '0':
            continue
        else:
            count += 1

    print(f"{ans1} {count}\n")
