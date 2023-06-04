n = int(input())
sum = 0
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort(reverse=True)

for i in range(n):
    sum += A[i] * B[i]
print(sum)
