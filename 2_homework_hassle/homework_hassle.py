# 2. Homework Hassle

N = int(input())
M = int(input())
T = list(map(int, input().split()))

T.sort()

ans = 0
for t in T:
    if t > M:
      break
    ans += 1
    M -= t

print(ans)