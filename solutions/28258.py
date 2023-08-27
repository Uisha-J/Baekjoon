import sys
flush = sys.stdout.flush


def find(x, y):
    if Q3 == True:
        print(f"? {x} {y+1}")
        flush()
        if int(input()) == 1:
            print(f"! {x} {y} {x} {y+1}")
            flush()
            exit()
        else:
            print(f"? {x+1} {y}")
            flush()
            if int(input()) == 1:
                print(f"! {x} {y} {x+1} {y}")
                flush()
                exit()
            else:
                print(f"? {x-1} {y}")
                flush()
                if int(input()) == 1:
                    print(f"! {x} {y} {x-1} {y}")
                    flush()
                    exit()
                else:
                    print(f"! {x} {y} {x} {y-1}")
                    flush()
                    exit()
    elif Q2 == True:
        if y == 0:
            print(f"? {x+1} {y}")
            flush()
            if int(input()) == 1:
                print(f"! {x} {y} {x+1} {y}")
                flush()
                exit()
            else:
                print(f"? {x-1} {y}")
                flush()
                if int(input()) == 1:
                    print(f"! {x} {y} {x-1} {y}")
                    flush()
                    exit()
                else:
                    print(f"! {x} {y} {x} {y+1}")
                    flush()
                    exit()
        elif y == 9:
            print(f"? {x+1} {y}")
            flush()
            if int(input()) == 1:
                print(f"! {x} {y} {x+1} {y}")
                flush()
                exit()
            else:
                print(f"? {x-1} {y}")
                flush()
                if int(input()) == 1:
                    print(f"! {x} {y} {x-1} {y}")
                    flush()
                    exit()
                else:
                    print(f"! {x} {y} {x} {y-1}")
                    flush()
                    exit()
        if x == 0:
            print(f"? {x} {y+1}")
            flush()
            if int(input()) == 1:
                print(f"! {x} {y} {x} {y+1}")
                flush()
                exit()
            else:
                print(f"? {x} {y-1}")
                flush()
                if int(input()) == 1:
                    print(f"! {x} {y} {x} {y-1}")
                    flush()
                    exit()
                else:
                    print(f"! {x} {y} {x+1} {y}")
                    flush()
                    exit()
        elif x == 9:
            print(f"? {x} {y+1}")
            flush()
            if int(input()) == 1:
                print(f"! {x} {y} {x} {y+1}")
                flush()
                exit()
            else:
                print(f"? {x} {y-1}")
                flush()
                if int(input()) == 1:
                    print(f"! {x} {y} {x} {y-1}")
                    flush()
                    exit()
                else:
                    print(f"! {x} {y} {x-1} {y}")
                    flush()
                    exit()
    return


Q3 = True

for i in range(1, 9):
    for j in range(1, 9):
        if (i % 2 == 0 and j % 2 == 0) or (i % 2 != 0 and j % 2 != 0):
            print(f"? {i} {j}")
            flush()
            if int(input()) == 1:
                find(i, j)
            else:
                continue

Q3 = False

Q2 = True
xlst = [2, 4, 6, 8, 9, 0, 9, 0, 9, 0, 9, 0, 1, 3, 5, 7]
ylst = [0, 0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 9, 9]

for i in range(16):
    print(f"? {xlst[i]} {ylst[i]}")
    flush()
    if int(input()) == 1:
        find(xlst[i], ylst[i])
    else:
        continue
Q2 = False

print(f"? 0 0")
if int(input()) == 1:
    print(f"? 0 1")
    flush()
    if int(input()) == 1:
        print(f"! 0 0 0 1")
        flush()
        exit()
    else:
        print(f"! 0 0 1 0")
        flush()
        exit()
else:
    print(f"? 9 8")
    flush()
    if int(input()) == 1:
        print(f"! 9 8 9 9")
        flush()
        exit()
    else:
        print(f"! 8 9 9 9")
        flush()
        exit()
