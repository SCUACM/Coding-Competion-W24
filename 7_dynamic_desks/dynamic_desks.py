# 7. Dynamic Desks

N, S = map(int, input().split())

dp = [0] * (N+1)
dp[1] = 2
for i in range(2, N+1):
  dp[i] = dp[i-1] + (dp[i-S-1] if i >= S+2 else 1)

print(dp[N])