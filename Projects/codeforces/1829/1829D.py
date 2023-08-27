import sys
input = sys.stdin.readline
print = sys.stdout.write

for i in range(int(input())):
    A, B = map(int, input().split())
    find = False
    if A < B:
        find = False
    else:
        if A == B:
            find = True
        else:
            Acount = 0
            Bcount = 0
            while B % 3 == 0:
                B //= 3
                Bcount += 1
            for i in range(Bcount):
                B *= 3
            while A % 3 == 0:
                A //= 3
                Acount += 1
            for i in range(Acount):
                A *= 3
            for i in range(Acount - Bcount):
                A //= 3
            for i in range(Acount - Bcount + 1):
                if A == B:
                    find = True
                    break
                else:
                    A *= 2
    if find == True:
        print('YES\n')
    else:
        print('NO\n')
