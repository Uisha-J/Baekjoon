import sys
input = sys.stdin.readline
print = sys.stdout.write


n, m, q = map(int, input().split())
matrix = [[0] * m for _ in range(n)]
print(matrix)

for i in range(m):
    q_type, idx, v = map(int, input().split())
    idx -= 1

    if q_type == 1:
        matrix[idx] = [x + v for x in matrix[idx]]
    else:
        for i in range(len(matrix)):
            matrix[i][idx] += v

    for row in matrix:
        print(''.join(row))

for row in matrix:
    print(''.join(map(str, row)))
