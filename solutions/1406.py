import sys
from collections import deque

input = sys.stdin.readline
print = sys.stdout.write

text = input().rstrip()
left_part = deque(text)
right_part = deque()

n = int(input())

for i in range(n):
    command = input().split()
    if command[0] == 'L' and left_part:
        right_part.appendleft(left_part.pop())
    elif command[0] == 'D' and right_part:
        left_part.append(right_part.popleft())
    elif command[0] == 'B' and left_part:
        left_part.pop()
    elif command[0] == 'P':
        left_part.append(command[1])

print(''.join(left_part + right_part))
