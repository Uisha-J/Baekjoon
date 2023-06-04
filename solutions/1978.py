N = int(input())
numlist = list(map(int, input().split()))
count = 0


def primenumber(k):
    for i in range(2, k):
        if k % i == 0:
            return False
    return True


for i in range(N):
    if primenumber(numlist[i]) == True and numlist[i] != 1:
        count += 1

print(count)
