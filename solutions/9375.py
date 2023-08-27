import sys
input = sys.stdin.readline
print = sys.stdout.write

for _ in range(int(input())):
    wear = []
    for i in range(int(input())):
        a, b = input().split()
        wear.append(b)
    if len(wear) == 0:
        print('0\n')
        continue
    elif len(set(wear)) == 1:
        print(f'{len(wear)}\n')
        continue
    weartype = len(set(wear))
    A = []
    for i in set(wear):
        A.append(wear.count(i))
    ans = A[0] + 1
    for i in range(1, len(A)):
        ans *= A[i] + 1
    print(f'{ans - 1}\n')
