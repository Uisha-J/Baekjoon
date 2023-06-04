import sys
input = sys.stdin.readline
print = sys.stdout.write

n, m = map(int, input().rstrip().split())
coin = 0
coinlist = []

for i in range(n):
    coinlist.append(int(input()))


def lower_bound(arr, x):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < x:
            left = mid + 1
        elif arr[mid] == x:
            left = mid + 1
        else:
            right = mid - 1
    return left


while m > 0:
    k = coinlist[lower_bound(coinlist, m)-1]
    if m % k == 0:
        coin += m // k
        m = 0
    else:
        m -= k
        coin += 1
print(str(coin))
