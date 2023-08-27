from collections import deque
import sys

input = sys.stdin.readline
print = sys.stdout.write

number = int(input())
visited = [False] * (number + 1)
graph = [[] for _ in range(number + 1)]
ans = 0
for i in range(int(input())):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
