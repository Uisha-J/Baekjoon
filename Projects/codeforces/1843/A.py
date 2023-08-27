import sys
input = sys.stdin.readline
print = sys.stdout.write

for i in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()

    if n == 1:
        print('0\n')
        continue

    ans = 0
    for i in range(n//2):
        ans += arr[-(i+1)] - arr[i]

    print(f"{ans}\n")
