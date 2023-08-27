def primecheck(num):
    global k

    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0:
        k = 2
        return False
    if num % 3 == 0:
        k = 3
        return False
    i = 5
    while i * i <= num:
        if num % i == 0:
            k = i
            return False
        if num % (i + 2) == 0:
            k = i + 2
            return False
        i += 6
    return True


n = int(input())

if n == 1:
    print(0)
elif primecheck(n) == True:
    print(n-1)
else:
    print(n - n / k)
