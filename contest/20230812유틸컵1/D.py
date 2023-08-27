from collections import deque


def q2(matrix):
    n = len(matrix)
    for i in range(n // 2):
        for j in range(i, n - i - 1):
            temp = matrix[i][j]
            matrix[i][j] = matrix[n - 1 - j][i]
            matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j]
            matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i]
            matrix[j][n - 1 - i] = temp


def q1(matrix, i):
    matrix[i - 1].insert(0, matrix[i - 1].pop())


n = int(input())
matrix = []
for _ in range(n):
    row = input().split()
    matrix.append(row)

q = int(input())
for _ in range(q):
    query = input().split()
    if query[0] == '1':
        num = int(query[1])
        q1(matrix, num)
    else:
        q2(matrix)

for row in matrix:
    print(' '.join(row))
