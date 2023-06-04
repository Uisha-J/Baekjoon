n = int(input())
count = 0

for _ in range(n):
    date = int(input().replace("D-",""))
    if date > 90:
        count += 1

print(n - count)