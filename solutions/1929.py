def primecheck(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True


def find(m, n):
    primes = [num for num in range(max(2, m), n + 1) if primecheck(num)]
    return primes


start, end = map(int, input().split())
ans = find(start, end)
for i in ans:
    print(i)
