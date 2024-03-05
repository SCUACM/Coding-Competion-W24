# 1. Premium Professor

N = int(input())
name = list(map(str, input().split()))
qual = list(map(float, input().split()))
diff = list(map(float, input().split()))

max_prof, max_score = -1, float('-inf')
for i in range(N):
  score = qual[i] + (5.0 - diff[i])
  if score > max_score:
    max_score = score
    max_prof = i

print(name[max_prof])