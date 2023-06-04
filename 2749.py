import sys

n = int(sys.stdin.readline())
dp = [0, 1]

for i in range(2, (1500000)):
    dp.append((dp[i-1] + dp[i-2]))
    dp[i] %= 1000000

print(dp[n % 1500000])
