def is_possible(X):
    total = 0

    for i in lst:
        total += max(i - X, 0)

    return total >= M


N, M = map(int, input().split())
lst = list(map(int, input().split()))

start = 0
end = 10000000000

while start <= end:
    mid = (start + end) // 2

    if is_possible(mid):
        start = mid + 1
    else:
        end = mid - 1

print(end)
