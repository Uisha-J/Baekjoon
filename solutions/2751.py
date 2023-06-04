import sys
input = sys.stdin.readline

num = []
for i in range(int(input())):
    num.append(int(input()))

num.sort()
num = map(str, num)
print('\n'.join(num))
