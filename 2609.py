import sys

a, b = sys.stdin.readline().split()
a = int(a)
b = int(b)

for i in range(min(a, b),0,-1):
    if a%i == 0 and b%i == 0:
        print(i)
        gcd = i
        break

print(a*b//gcd)