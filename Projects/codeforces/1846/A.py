import sys
input = sys.stdin.readline
print = sys.stdout.write

for i in range(int(input())):
    cut = 0
    for i in range(int(input())):
        a, b = map(int, input().split())
        if a > b:
            cut += 1
    print(cut)
