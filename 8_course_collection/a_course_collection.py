# 8. Course Collection (Backtracking Approach)

import collections

def recursion(frontier, current):
    global scores
    global adjacent
    global n

    node = frontier.pop()
    current.append(node)
    if len(current) == n:
        scores.append(sum([int(values[x]) for x in current]))
        current.pop()
        return
    frontier = frontier + adjacent[node]
    
    for i in reversed(range(len(frontier))):
        recursion(frontier[:i + 1], current)
    current.pop()
    return
    
n, total = list(map(int, input().split()))
if n == total:
    print(sum(list(map(int, input().split()))))
    exit()
adjacent = collections.defaultdict(list)
for i in range(total - 1):
    h = list(map(int, input().split()))
    adjacent[h[0]].append(h[1])
values = list(map(int, input().split()))
scores = []
current = []
frontier = [0]

recursion(frontier, current)
print(max(scores))
