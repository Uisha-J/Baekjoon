import sys
print = sys.stdout.write
input = sys.stdin.readline

a = [0] * 10001

for i in range(int(input())):
    a[int(input())] += 1

for i in range(1, 10001):
    for _ in range(a[i]):
        print(f"{i}\n")
