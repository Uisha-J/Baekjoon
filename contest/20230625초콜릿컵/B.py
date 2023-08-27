from collections import deque

dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]
bugs = 0


def bfs(graph, y, x):
    queue = deque()
    queue.append((y, x))
    graph[y][x] = 0

    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if nx < 0 or nx >= X or ny < 0 or ny >= Y:
                continue
            if graph[ny][nx] == 1:
                graph[ny][nx] = 0
                queue.append((ny, nx))


for _ in range(int(input())):
    bugs = 0
    check = list(map(int, input().split()))
    field = []
    field.append(list(input()))
    field.append(list(input()))
    field.append(list(input()))

    print(bugs)
