import sys
input = sys.stdin.readline

A, B, C = map(int, input().split())


def expon(a, n):
    if n == 1:
        return a % C

    e = expon(a, n//2)

    if n % 2 == 0:
        return e * e % C

    else:
        return e * e * a % C


print(expon(A, B))
