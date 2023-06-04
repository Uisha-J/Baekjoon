queue = []
arr = []

n, k = map(int, input().split())
k_temp = k - 1

for i in range(1, n+1):
    queue.append(i)

for i in range(n):
    arr.append(queue[k_temp])
    del (queue[k_temp])
    if len(queue) == 0:
        break
    k_temp = (k_temp + k - 1) % len(queue)

arr = list(map(str, arr))
print('<' + str(', '.join(arr)) + '>')
