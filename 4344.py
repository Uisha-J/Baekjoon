import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
    score = 0
    over = 0
    arr = list(map(int, input().split()))
    avg = (sum(arr) - arr[0]) / arr[0]
    for j in range(arr[0]):
        if arr[j+1] > avg:
            over += 1
    print(str("{:.3f}".format(over / arr[0] * 100,))+'%')
