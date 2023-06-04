dp = [0] * 1001
dp_R_minus_pi = [0] * 320

dp[0] = 1
dp[1] = 1
dp[2] = 1
dp[3] = 1
dp_R_minus_pi[0] = 1

for i in range(4, 1001):
    dp[i] = dp[i-1] + dp_R_minus_pi[0]
    dp_R_minus_pi[i] = dp_R_minus_pi[i-1] + dp_R_minus_pi
