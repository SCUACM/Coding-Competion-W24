# 8. Course Collection (2D Dynamic Programming Approach)

N, M = map(int, input().split())
children = [[] for _ in range(M)]
for _ in range(M-1):
  parent, child = map(int, input().split())
  children[parent].append(child)
power = list(map(int, input().split()))

dp = [[0 for _ in range(N+1)] for _ in range(M)]
def dfs(node):
  dp[node][1] = power[node]
  for child in children[node]:
    dfs(child)
    for i in range(N, 0, -1):
      for j in range(i):
        dp[node][i] = max(dp[node][i], dp[node][i-j] + dp[child][j])

dfs(0)

print(dp[0][N])