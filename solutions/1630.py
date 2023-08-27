def sieve(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return [i for i, prime in enumerate(is_prime) if prime]


def lcm(start, end):
    primes = sieve(end)
    lcm = 1
    mod = 987654321
    for prime in primes:
        if prime >= start:
            power = 1
            while prime ** power <= end:
                power += 1
            lcm = (lcm * (prime ** (power - 1))) % mod
    return lcm


def smallest_multiple(n):
    return lcm(1, n)


n = int(input())
result = smallest_multiple(n)
print(result)
