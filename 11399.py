n = int(input())
timelist = list(map(int, input().split()))
timelist.sort()
for i in range(1, n):
    timelist[i] = timelist[i] + timelist[i-1]

print(sum(timelist))
