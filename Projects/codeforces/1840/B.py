import sys
input = sys.stdin.readline
print = sys.stdout.write

for i in range(int(input())):
    coin, menu = map(int, input().split())
    print(f'{min(coin + 1,2 ** min(menu, 64))} \n')
