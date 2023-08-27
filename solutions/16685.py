import sys
input = sys.stdin.readline


def find_largest_xor_sum(numbers):
    n = len(numbers)
    basis = []

    for i in range(n):
        x = numbers[i]
        for b in basis:
            if x ^ b < x:
                x ^= b
        if x != 0:
            basis.append(x)
    max_xor_sum = 0
    for b in basis:
        if max_xor_sum ^ b > max_xor_sum:
            max_xor_sum ^= b

    return max_xor_sum


numbers = []
for i in range(int(input())):
    numbers.append(int(input()))

for i in range(1, len(numbers)):
    numbers[i] = numbers[i] ^ numbers[0]
del (numbers[0])

print(find_largest_xor_sum(numbers))
