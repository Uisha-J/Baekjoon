import sys

Q = int(sys.stdin.readline())

for _ in range(Q):
    K = sys.stdin.readline().split()
    gcd = int(K[0])
    sum = int(K[1])

    if sum % gcd == 0 and sum != gcd:
        print("1")
    else:
        print("0")