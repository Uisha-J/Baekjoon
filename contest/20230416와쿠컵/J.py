import sys
input = sys.stdin.readline
print = sys.stdout.write

N, M = map(int, input().split())
candylist = list(map(int, input().split()))
for i in range(1, len(candylist)):
    candylist[i] = candylist[i] + candylist[i-1]


def lower_bound(arr, x):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return left


for i in range(N):
    candy = int(input())
    if candy <= candylist[-1]:
        print(str(lower_bound(candylist, candy) + 1) + '\n')
    else:
        print('Go away!\n')
