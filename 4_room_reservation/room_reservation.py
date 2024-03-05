# 4. Room Reservation

N = int(input())
segments = []
for i in range(N):
  segment = [(0,0), (24,24)]
  S = int(input())
  for _ in range(S):
    L, R = map(int, input().split())
    segment.append((L, R))
  segments.append(segment)

for s in segments:
  s.sort()

for s in segments:
  for i in range(0, len(s)-1):
    ans = max(ans, s[i+1][0] - s[i][1])

print(ans)