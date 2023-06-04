x1, y1 = map(input().split())
x2, y2 = map(input().split())

if x1 % 2 == 0:
    if y1 % 2 == 0:
        white1 = True
    else:
        white1 = False
else:
    if y1 % 2 == 0:
        white1 = False
    else:
        white1 = True

if x2 % 2 == 0:
    if y2 % 2 == 0:
        white2 = True
    else:
        white2 = False
else:
    if y2 % 2 == 0:
        white2 = False
    else:
        white2 = True

if white1 == white2:
    print('black')
else:
    print('white')
