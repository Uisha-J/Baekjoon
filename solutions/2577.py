A = int(input())
B = int(input())
C = int(input())
arr = A * B * C

arr = list(str(arr))
numberlist = [0] * 10

for i in range(len(arr)):
    N = int(arr[i])
    numberlist[N] += 1

for i in range(10):
    print(numberlist[i])