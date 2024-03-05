# 5. Increasingly Indoors

from collections import deque, defaultdict

D = int(input())
doors = []
for _ in range(D):
  a, b = map(int, input().split())
  doors.append((a,b))

adj = defaultdict(list)
for a, b in doors:
  if b not in adj[a]:
    adj[a].append(b)
    adj[b].append(a)

depth = -1
room = 0
visited = set([0])
frontier = deque([0])
while frontier:
  depth += 1
  rooms = list(frontier)
  for _ in range(len(frontier)):
    room = frontier.popleft()
    for adj_room in adj[room]:
      if adj_room not in visited:
        visited.add(adj_room)
        frontier.append(adj_room)

print(depth)
print(" ".join([str(r) for r in sorted(rooms)]))