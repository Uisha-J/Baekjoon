import sys
sys.setrecursionlimit(10000)

n = int(input())
original = n
times = 0


def cycle(n):
    global times
    global nlist
    if n < 10:
        n = int('0' + str(n))
        nlist = list(map(int, str(n)))
        n = sum(nlist)
        n = str(nlist[-1]) + str(list(map(int, str(n)))[-1])
        n = int(n)
        times += 1
        if n == original:
            print(times)
            sys.exit()
        else:
            cycle(n)
    else:
        nlist = list(map(int, str(n)))
        n = sum(nlist)
        n = str(nlist[-1]) + str(list(map(int, str(n)))[-1])
        n = int(n)
        times += 1
        if n == original:
            print(times)
            sys.exit()
        else:
            cycle(n)


cycle(n)
