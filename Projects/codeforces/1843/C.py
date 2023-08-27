import sys
input = sys.stdin.readline
print = sys.stdout.write

for i in range(int(input())):
    n = int(input())
    sum = 0
    sum += n
    while n > 1:
        sum += (n // 2)
        n = n // 2
    print(f"{sum}\n")
