n = int(input())

for i in range(n):
    dp = [1, 1]
    m, k = map(int, input().split())
    for i in range(2, k**2 - 1):
        dp.append(dp[i-2] + dp[i-1])
        dp[i] %= k
        dp = list(set(dp))
        print(len(dp))
