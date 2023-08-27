def replace_missing_numbers(sequence, l, r, k, replacement):
    has_all_numbers = all(1 <= num <= k for num in sequence[l-1:r])

    if not has_all_numbers:
        for i in range(l-1, r):
            sequence[i] = replacement


n, m = map(int, input().split())
arr = [0] * n

for i in range(m):
    l, r = map(int, input().split())
    k = r - l + 1
    for i in range(k):
        if i + 1 not in arr[l:r]:
            arr[l:r] = []

print(arr)
