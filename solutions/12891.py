n, m = map(int, input().split())
arr = input()
standard = list(map(int, input().split()))

initial_counts = [0] * 4
for i in range(m):
    if arr[i] == 'A':
        initial_counts[0] += 1
    elif arr[i] == 'C':
        initial_counts[1] += 1
    elif arr[i] == 'G':
        initial_counts[2] += 1
    elif arr[i] == 'T':
        initial_counts[3] += 1

if initial_counts[0] >= standard[0] and initial_counts[1] >= standard[1] and \
        initial_counts[2] >= standard[2] and initial_counts[3] >= standard[3]:
    count = 1
else:
    count = 0

for i in range(1, n - m + 1):
    if arr[i - 1] == 'A':
        initial_counts[0] -= 1
    elif arr[i - 1] == 'C':
        initial_counts[1] -= 1
    elif arr[i - 1] == 'G':
        initial_counts[2] -= 1
    elif arr[i - 1] == 'T':
        initial_counts[3] -= 1

    if arr[i + m - 1] == 'A':
        initial_counts[0] += 1
    elif arr[i + m - 1] == 'C':
        initial_counts[1] += 1
    elif arr[i + m - 1] == 'G':
        initial_counts[2] += 1
    elif arr[i + m - 1] == 'T':
        initial_counts[3] += 1

    if initial_counts[0] >= standard[0] and initial_counts[1] >= standard[1] and \
            initial_counts[2] >= standard[2] and initial_counts[3] >= standard[3]:
        count += 1

print(count)
