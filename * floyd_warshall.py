INF = int(1e9)

# node, edge
n = int(input())
m = int(input())

graph = [[INF] * (n + 1) for _ in range(n + 1)]

# value when go to me is 0
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

# give information, initialization
for _ in range(m):
    # value when to b from a is c
    a, b, c = map(int, input().split())
    graph[a][b] = c

# floyd warshall
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[b][k])

# return result
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if graph[a][b] == INF:
            print('INFINITY', end = " ")
        else:
            print(graph[a][b], end = " ")
    print()