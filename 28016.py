import copy

N, M = map(int, input().split())
arr = [[0 for j in range(M)] for i in range(N)]

for i in range(N):
    arr[i] = list(map(int, input().split()))

bolt = 0
for i in range(N):
    bolt += arr[i].count(1)

start = arr[0].index(2)
dp1 = copy.deepcopy(arr[0])
dp1[start] = 2 ** (bolt + 1)

for i in range(1, N):
    if i % 2 == 1:
        dp2 = copy.deepcopy(arr[i])
        for j in range(M):
            if dp1[j] >= 2:
                leftblock = False
                rightblock = False
                if dp2[j] != 1:
                    dp2[j] += dp1[j]
                else:
                    if dp2[j] == 1:
                        if dp1[j-1] == 1 or dp2[j-1] == 1:
                            leftblock = True
                        if dp1[j+1] == 1 or dp2[j+1] == 1:
                            rightblock = True
                    if leftblock == True and rightblock == False:
                        dp2[j+1] += dp1[j] // 2
                    elif leftblock == False and rightblock == True:
                        dp2[j-1] += dp1[j] // 2
                    elif leftblock == True and rightblock == True:
                        pass
                    else:
                        dp2[j-1] += dp1[j] // 2
                        dp2[j+1] += dp1[j] // 2
    elif i % 2 == 0:
        dp1 = copy.deepcopy(arr[i])
        for j in range(M):
            if dp2[j] >= 2:
                leftblock = False
                rightblock = False
                if dp1[j] != 1:
                    dp1[j] += dp2[j]
                else:
                    if dp1[j] == 1:
                        if dp2[j-1] == 1 or dp1[j-1] == 1:
                            leftblock = True
                        if dp2[j+1] == 1 or dp1[j+1] == 1:
                            rightblock = True
                    if leftblock == True and rightblock == False:
                        dp1[j+1] += dp2[j] // 2
                    elif leftblock == False and rightblock == True:
                        dp1[j-1] += dp2[j] // 2
                    elif leftblock == True and rightblock == True:
                        pass
                    else:
                        dp1[j-1] += dp2[j] // 2
                        dp1[j+1] += dp2[j] // 2

if N % 2 == 0:
    if max(dp2) == 1 or max(dp2) == 0:
        print('-1')
    else:
        print(dp2.index(max(dp2)))
else:
    if max(dp1) == 1 or max(dp1) == 0:
        print('-1')
    else:
        print(dp1.index(max(dp1)))
