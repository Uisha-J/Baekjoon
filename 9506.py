import sys
import math
input = sys.stdin.readline


def getMyDivisor(n):

    divisorsList = []

    for i in range(1, int(n**(1/2)) + 1):
        if (n % i == 0):
            divisorsList.append(i)
            if ((i**2) != n):
                divisorsList.append(n // i)

    divisorsList.sort()

    return divisorsList


while True:
    k = int(input())
    if k == -1:
        exit()
    arr = getMyDivisor(k)
    del (arr[-1])
    if sum(arr) == k:
        arr = list(map(str, arr))
        print(k, '=', ' + '.join(arr))
    else:
        print(k, 'is NOT perfect.')
