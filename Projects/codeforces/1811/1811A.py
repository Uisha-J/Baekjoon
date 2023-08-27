import sys
input = sys.stdin.readline
debug = print
print = sys.stdout.write

n = int(input())

for i in range(n):
    a, b = map(int, input().split())
    arr = list(map(int, input().strip()))
    answer = []
    B = False
    for j in range(int(a)):
        if min(arr) >= b:
            arr.insert(-1, b)
            break
        elif int(arr[j]) < int(b):
            arr.insert(j, b)
            break
    for i in range(len(arr)):
        print(arr[i])
