import sys


def count_twos(n):
    count = 0
    while n % 2 == 0 and n != 0:
        n = n // 2
        count += 1
    return count


def count_threes(n):
    count = 0
    while n % 3 == 0 and n != 0:
        n = n // 3
        count += 1
    return count


n = int(input())

arr = list(map(int, input().split()))

for i in range(len(arr)):
    arr[i] = (arr[i], count_twos(arr[i]), count_threes(arr[i]))

arr = sorted(arr, key=lambda x: (x[1], -x[2]))

ans = []
for i in range(len(arr)):
    ans.append(arr[i][0])

print(*ans)
