import sys
input = sys.stdin.readline
print = sys.stdout.write

for i in range(int(input())):
    arr = input()
    count = 0
    if arr[0] != 'c':
        count += 1
    if arr[1] != 'o':
        count += 1
    if arr[2] != 'd':
        count += 1
    if arr[3] != 'e':
        count += 1
    if arr[4] != 'f':
        count += 1
    if arr[5] != 'o':
        count += 1
    if arr[6] != 'r':
        count += 1
    if arr[7] != 'c':
        count += 1
    if arr[8] != 'e':
        count += 1
    if arr[9] != 's':
        count += 1
    print(str(count) + '\n')
