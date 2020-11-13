# floyd warshall
# start = 1, middle_node = k, goal = x
# shortest path

# company number, path number
n, m = map(int, input().split())
INF = int(1e9)
path = [[INF] * (n + 1) for i in range(n + 1)]

# value of to self is 0
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            path[a][b] = 0

# insert path
for _ in range(m):
    a, b = map(int, input().split())
    path[a][b] = 1
    path[b][a] = 1

# goal, middle_node
x, k = map(int, input().split())

# floyd
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            path[a][b] = min(path[a][b], path[a][k] + path[k][b])

## I worng thinking... this is aleady perfect floyd warshall..
## Just print (value of to k form a + value of to b from a)...
# to_k = INF
# to_x = INF
# result = INF
# for i in range(1, n + 1):
#     to_k = min(to_k, path[1][k], path[1][i] + path[k][i])
#     to_x = min(to_x, path[k][x], path[k][i] + path[x][i])
#
#     result = min(result, to_k + to_x)
#
# print(result)

distance = path[1][k] + path[k][x]
if distance == INF:
    print(-1)
else:
    print(distance)