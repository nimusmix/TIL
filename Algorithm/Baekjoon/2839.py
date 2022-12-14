N = int(input())

dp = [5000] * 5001
dp[3] = dp[5] = 1
for i in range(6, N+1):
    dp[i] = min(dp[i-3], dp[i-5]) + 1

print(-1 if dp[N] >= 5000 else dp[N])