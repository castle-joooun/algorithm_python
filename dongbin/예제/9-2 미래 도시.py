INF = int(1e9)

n, m = map(int, input().split())
graph = [[INF] * (n + 1) for _ in range(n + 1)]

for a in range(n + 1):
    for b in range(n + 1):
        if a == b:
            graph[a][b] = 0

for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

end, mid = map(int, input().split())

for k in range(n + 1):
    for a in range(n + 1):
        for b in range(n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

distance = graph[1][mid] + graph[mid][end]

if distance >= INF:
    print(-1)
else:
    print(distance)

# if graph[1][mid] == INF:
#     print(-1)
# elif graph[mid][end] == INF:
#     print(-1)
# else:
#     print(graph[1][mid] + graph[mid][end])
