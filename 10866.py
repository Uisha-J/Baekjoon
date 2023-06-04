import sys
input = sys.stdin.readline

deck = []
n = int(input())

for i in range(n):
    execute = list(input().split())
    if execute[0] == 'push_front':
        deck.insert(0, execute[1])
    elif execute[0] == 'push_back':
        deck.append(execute[1])
    elif execute[0] == 'back':
        if len(deck) == 0:
            print('-1')
        else:
            print(deck[-1])
    elif execute[0] == 'front':
        if len(deck) == 0:
            print('-1')
        else:
            print(deck[0])
    elif execute[0] == 'pop_back':
        try:
            print(deck[-1])
            deck.pop()
        except:
            print('-1')
    elif execute[0] == 'pop_front':
        try:
            print(deck[0])
            deck.pop(0)
        except:
            print('-1')
    elif execute[0] == 'size':
        print(len(deck))
    elif execute[0] == 'empty':
        if len(deck) == 0:
            print('1')
        else:
            print('0')
