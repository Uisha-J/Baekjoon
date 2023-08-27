from collections import deque


def bfs(start):
    global visited
    q = deque()
    visited[start] = True
    q.append(start)

    while q:
        x = q.popleft()

        for i in graph[x]:
            if visited[i] == False:
                q.append(i)
                visited[i] = True


k, j = map(int, input().split())
visited = [False] * (k + 1)
graph = [[] for _ in range(k + 1)]
count = 0

for i in range(j):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


for i in range(1, k+1):
    if visited[i] == True:
        continue
    bfs(i)
    count += 1

print(count)
