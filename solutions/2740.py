import sys
input = sys.stdin.readline


def matrix_multiply(matrix1, matrix2):
    rows1 = len(matrix1)
    cols1 = len(matrix1[0])
    rows2 = len(matrix2)
    cols2 = len(matrix2[0])

    result = [[0] * cols2 for _ in range(rows1)]

    for i in range(rows1):
        for j in range(cols2):
            for k in range(cols1):
                result[i][j] += matrix1[i][k] * matrix2[k][j]

    return result


n, m = map(int, input().split())
matrix1 = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix1.append(row)

m, k = map(int, input().split())
matrix2 = []
for _ in range(m):
    row = list(map(int, input().split()))
    matrix2.append(row)

result = matrix_multiply(matrix1, matrix2)

for row in result:
    print(*row)
