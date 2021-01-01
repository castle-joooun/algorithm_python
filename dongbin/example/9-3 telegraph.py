import heapq

# city number, path number, start city
n, m, c = map(int, input().split())

INF = int(1e9)
path = [[] for i in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    # from x, to y, value z
    x, y, z = map(int, input().split())
    path[x].append((y, z))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in path[now]:
            cost = dist + i[now]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(c)

count = 0
max_value = 0

for i in range(1, n + 1):
    if distance[i] != INF and i != c:
        count += 1
        if max_value < distance[i]:
            max_value = distance[i]

print(count, max_value)