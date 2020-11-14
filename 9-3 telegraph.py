# city number, path number, goal city
n, m, c = map(int, input().split())

INF = int(1e9)
path = [[INF] * (n + 1) for i in range(n + 1)]
visited = [False] * (n + 1)
distance = [INF] * (n + 1)

for _ in range(m):
    # from x, to y, value z
    x, y, z = map(int, input().split())
    path[x] = (y, z)