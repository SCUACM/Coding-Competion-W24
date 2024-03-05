# 3. Silence, Swig

N = int(input())
V = list(map(float, input().split()))

min_room = -1
min_score = float('inf')
for i in range(N):
  score = 0
  for j in range(N):
    if i == j:
      continue
    score += V[j] / abs(i - j)
  if score < min_score:
    min_score = score
    min_room = i

print(min_room)