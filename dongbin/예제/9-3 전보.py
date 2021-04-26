import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m, c = map(int, input().split())
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))

q = []
heapq.heappush(q, (0, c))
distance[c] = 0

while q:
    dist, now = heapq.heappop(q)

    if dist > distance[now]:
        continue
    for i in graph[now]:
        cost = dist + i[1]
        if cost < distance[i[0]]:
            distance[i[0]] = cost
            heapq.heappush(q, (cost, i[0]))

count = 0
time = 0
for x in distance:
    if x != INF:
        count += 1
        time = max(time, x)

print(count - 1, time)
