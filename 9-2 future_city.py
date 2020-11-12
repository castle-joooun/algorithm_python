# floyd warshall
# start = 1, middle_node = k, goal = x
# shortest path

# company number, path number
n, m = map(int, input().split())
INF = int(1e9)
path = [[INF] * (m + 1) for i in range(m + 1)]

# insert path
for i in range(1, m + 1):
    a, b = map(int, input().split())
    path[a][b] = 1

# goal, middle_node
x, k = map(int, input().split())

# floyd
for k in range(1, m + 1):
    for a in range(1, m + 1):
        for b in range(1, m + 1):
            path[a][b] = min(path[a][b], path[a][k] + path[b][k])

to_k = INF
to_x = INF
result = INF
for i in range(1, m + 1):
    to_k = min(to_k, path[1][k], path[1][i] + path[k][i])
    to_x = min(to_x, path[k][x], path[k][i] + path[x][i])

    result = min(result, to_k + to_x)

print(result)
