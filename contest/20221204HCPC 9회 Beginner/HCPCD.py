import sys

Y = int(sys.stdin.readline().rstrip())
X = int(input())

if Y % 4 == 0 and Y % 100 != 0:
    print('30')
elif Y % 400 == 0:
    print('30')
else:
    print('29')