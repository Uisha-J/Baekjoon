N = int(input())
original = N
token = 0

if N <= 15:
    if N == 3:
        print('1')
    elif N == 4:
        print('-1')
    elif N == 5:
        print('1')
    elif N == 6:
        print('2')
    elif N == 7:
        print('-1')
    elif N == 8:
        print('2')
    elif N == 9:
        print('3')
    elif N == 10:
        print('2')
    elif N == 11:
        print('3')
    elif N == 12:
        print('4')
    elif N == 13:
        print('3')
    elif N == 14:
        print('4')
    elif N == 15:
        print('3')

while N > 15:
    N -= 5
    token += 1

if N <= 15 and original > 15:
    if N == 11:
        print(token + 3)
    elif N == 12:
        print(token + 4)
    elif N == 13:
        print(token + 3)
    elif N == 14:
        print(token + 4)
    elif N == 15:
        print(token + 3)
