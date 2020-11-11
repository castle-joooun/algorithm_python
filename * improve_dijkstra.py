import heapq
import sys

input = sys.stdin.readline()
INF = int(1e9)

# node, edge
n, m = map(int, input().split())
start = int(input())
graph = [[] for i in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    # value when to b from a is c
    graph[a].append((b, c))

def dijkstra(start):
    q = []
    # shortest path is 0 for start node, insert queue
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q: # if queue isn't empty
        # this is popping value of shortest path
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(start)

for i in range(1, n + 1):
    if distance[i] == INF:
        print('INFINITY')
    else:
        print(distance[i])

