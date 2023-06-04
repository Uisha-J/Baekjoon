from collections import deque


def bfs(start):
    global ans

    q = deque()
    visited[start] = True
    q.append(start)

    while q:
        x = q.popleft()

        for i in graph[x]:
            if visited[i] == False:
                q.append(i)
                visited[i] = True
                ans += 1


number = int(input())
visited = [False] * (number + 1)
graph = [[] for _ in range(number + 1)]
ans = 0

for i in range(int(input())):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

bfs(1)

print(ans)
