n = int(input())
dp = [0]*81

dp[0] = 0
dp[1] = 1

for i in range(2, n+1):
    dp[i] = dp[i-2] + dp[i-1]

print(dp[n] * 4 + dp[n-1] * 2)
