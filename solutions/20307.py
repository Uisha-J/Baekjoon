from fractions import Fraction
def rref(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    pivot_columns = []  # 선행 지수가 있는 열의 인덱스 저장
    for i in range(rows):
        # 행렬에서 선행 지수 찾기
        pivot_index = -1  # 피봇의 열 인덱스
        for j in range(cols):
            if matrix[i][j] != 0:
                pivot_index = j
                break

        if pivot_index == -1:  # 선행 지수가 없는 행인 경우 종료
            break

        pivot_columns.append(pivot_index)

        # 피봇의 열을 1로 만들기
        pivot_value = matrix[i][pivot_index]
        for j in range(cols):
            matrix[i][j] /= pivot_value

        # 피봇 이외의 열 요소들을 0으로 만들기
        for k in range(rows):
            if k != i:
                factor = matrix[k][pivot_index]
                for j in range(cols):
                    matrix[k][j] -= factor * matrix[i][j]

    # 선행 지수가 있는 열 이외의 요소들을 0으로 만들기
    for i in range(rows):
        for j in range(cols):
            if j not in pivot_columns:
                matrix[i][j] = 0

    return matrix


rows, cols = map(int,input().split())

matrix = []
for i in range(rows):
    row = input().split()
    row = [Fraction(element) for element in row]  # 분수로 변환
    matrix.append(row)

# 가우스 소거법 실행
rref_matrix = rref(matrix)

# 결과 출력
for row in rref_matrix:
    lst = row
    result = []
    for element in lst:
        if isinstance(element, Fraction):
            if element.denominator == 1:
                result.append(str(element.numerator))
            else:
                result.append(str(element.numerator) + '/' + str(element.denominator))
        else:
            result.append(str(element))
    result_str = ' '.join(result)
    print(result_str)