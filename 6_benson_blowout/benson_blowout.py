# 6. Benson Blowout

P = int(input())
N = int(input())
prices = list(map(float, input().split()))

P = round(P * 100)
prices = [round(p * 100) for p in prices]

p_max = 0
def dfs(p, i):
  global p_max
  if i >= N or p > P:
    return
  p_max = max(p_max, p)
  dfs(p + prices[i], i)
  dfs(p, i + 1)

dfs(0, 0)

print("{:.2f}".format((P - p_max) / 100))