from collections import deque

dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]


def bfs(graph, y, x):

    queue = deque()
    queue.append((y, x, 1))
    graph[y][x] = 0
    while queue:
        y, x, d = queue.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if nx < 0 or nx >= X or ny < 0 or ny >= Y:
                continue
            if graph[ny][nx] == 1:
                graph[ny][nx] = 0
                queue.append((ny, nx, d+1))
                if nx == X-1 and ny == Y-1:
                    return d + 1


maze = []
Y, X = map(int, input().split())
for i in range(Y):
    maze.append(list(map(int, (input()))))
print(bfs(maze, 0, 0))
