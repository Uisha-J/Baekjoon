from collections import deque

way = int(input())
reach, dps = map(int, input().split())
m16 = int(input())
dq = deque()


for i in range(way):
    dq.append(int(input()))

print(dq)
