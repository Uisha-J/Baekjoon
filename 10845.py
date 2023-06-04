import sys
input = sys.stdin.readline

stack = []
n = int(input())

for i in range(n):
    execute = list(input().split())
    if execute[0] == 'push':
        stack.append(execute[1])
    elif execute[0] == 'front':
        if len(stack) == 0:
            print('-1')
        else:
            print(stack[0])
    elif execute[0] == 'back':
        if len(stack) == 0:
            print('-1')
        else:
            print(stack[-1])
    elif execute[0] == 'pop':
        try:
            print(stack[0])
            del stack[0]
        except:
            print('-1')
    elif execute[0] == 'size':
        print(len(stack))
    elif execute[0] == 'empty':
        if len(stack) == 0:
            print('1')
        else:
            print('0')
