def gaussian_elimination(matrix, vector):
    rows = len(matrix)
    cols = len(matrix[0])

    for i in range(rows):
        if matrix[i][i] == 0:
            for j in range(i + 1, rows):
                if matrix[j][i] != 0:
                    matrix[i], matrix[j] = matrix[j], matrix[i]
                    vector[i], vector[j] = vector[j], vector[i]
                    break
            else:
                return None

        pivot = matrix[i][i]

        for j in range(i, cols):
            matrix[i][j] /= pivot

        vector[i] /= pivot

        for j in range(rows):
            if j != i:
                factor = matrix[j][i]
                for k in range(i, cols):
                    matrix[j][k] -= factor * matrix[i][k]
                vector[j] -= factor * vector[i]

    return vector


n = int(input())
matrix = []
vector = []

for _ in range(n):
    equation = input()
    coefficients = list(map(float, equation.split()))
    matrix.append(coefficients[:-1])
    vector.append(coefficients[-1])

result = gaussian_elimination(matrix, vector)
ans = []

for i, x in enumerate(result):
    ans.append(x)

for i in range(n):
    if int(ans[i]) == ans[i]:
        ans[i] = int(ans[i])
    else:
        ans[i] = round(ans[i], 3)
        if int(ans[i]) == ans[i]:
            ans[i] = int(ans[i])

print(*ans)
