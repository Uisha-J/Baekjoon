import sys
input = sys.stdin.readline
print = sys.stdout.write

for i in range(int(input())):
    book = []
    left = []
    right = []
    all = []
    for i in range(int(input())):
        K = input().split()
        if K[1] == '10':
            left.append(int(K[0]))
        elif K[1] == '01':
            right.append(int(K[0]))
        elif K[1] == '11':
            all.append(int(K[0]))
    try:
        P = min(left) + min(right)
        leftright = True
    except:
        leftright = False
    if leftright == False and len(all) != 0:
        M = min(all)
        print(str(M) + '\n')
    elif leftright == True and len(all) != 0:
        M = min(all)
        print(str(min(M, P)) + '\n')
    elif leftright == True and len(all) == 0:
        print(str(P) + '\n')
    elif leftright == False and len(all) == 0:
        print('-1\n')
