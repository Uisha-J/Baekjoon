import sys
sys.setrecursionlimit(10**6)

N = int(input())
A = 0
B = 1
token = 1

if N == 1:
    print('1')
    sys.exit()


def find(N):
    global A
    global B
    global token
    if 6 * A + 2 <= N <= 6 * B + 1:
        print(token + 1)
    else:
        A += token
        B += token + 1
        token += 1
        find(N)


find(N)
