N = int(input())
S = [int(input()) for i in range(N)]

dp = [0] * N

if len(S) <= 2:
    dp[0] = S[0]
    if len(S) == 2:
        dp[1] = S[0]+S[1]

else:
    dp[0] = S[0]
    dp[1] = S[0]+S[1]

    for i in range(2, N):
        dp[i] = max(dp[i-3] + S[i-1] + S[i], dp[i-2] + S[i])

print(dp[-1])
