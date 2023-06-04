import sys
input = sys.stdin.readline
print = sys.stdout.write

arr = set()

for i in range(int(input())):
    command = list(input().split())
    if command[0] == 'add':
        arr.add(command[1])
    elif command[0] == 'remove':
        if command[1] in arr:
            arr.remove(command[1])
        else:
            pass
    elif command[0] == 'check':
        if command[1] in arr:
            print('1\n')
        else:
            print('0\n')
    elif command[0] == 'toggle':
        if command[1] in arr:
            arr.remove(command[1])
        else:
            arr.add(command[1])
    elif command[0] == 'all':
        arr = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
               '11', '12', '13', '14', '15', '16', '17', '18', '19', '20'}
    elif command[0] == 'empty':
        arr = set()
