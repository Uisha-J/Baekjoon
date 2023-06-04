n = int(input())
k = 0
j = 0
for i in range(1, n+1):
    print(i ** 2)
    k += i ** 2

print(k)

if n >= 3:
    j = ((n-2) ** 2) - (n-3)
    print("시발" + str(j))

print(k-j)
