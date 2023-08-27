import sys
input = sys.stdin.readline
print = sys.stdout.write

for i in range(int(input())):
    arrlen = int(input())
    arr = input()
    decrypted = []
    check = 0
    for j in range(arrlen):
        if check == 0:
            check = arr[j]
        elif arr[j] == check:
            decrypted.append(check)
            check = 0
        else:
            pass
    print(''.join(decrypted) + '\n')
