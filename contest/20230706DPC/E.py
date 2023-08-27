def multiply(a, b, m):
    return (a * b) % m

def power(base, exponent, m):
    if exponent == 0:
        return 1
    
    if exponent % 2 == 0:
        half = power(base, exponent // 2, m)
        result = multiply(half, half, m) % m
        print("Intermediate Result:", result)
        return result
    else:
        half = power(base, (exponent - 1) // 2, m)
        result = multiply(half, half, m) % m
        result = multiply(result, base, m) % m
        print("Intermediate Result:", result)
        return result

a, b = map(int, input().split())

m = int(1e9)  # 모듈러 값

result = a % m  # 초기값을 a의 모듈러 연산 값으로 설정
print("Intermediate Result:", result)

result = power(result, b, m)

digitCount = len(str(result))
print(digitCount)
