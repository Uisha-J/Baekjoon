num = [0] * 10000001

for i in range(1000001):
    num[i] = i

n = int(input())

if n == 1 or n == 2:
    print(1)
    exit()

start = 1
end = 1
count = 0

while start <= n // 2 + 1:
    current = (start + end) * (end - start + 1) // 2

    if current == n:
        count += 1
        start += 1
    elif current < n:
        end += 1
    else:
        start += 1

print(count + 1)
