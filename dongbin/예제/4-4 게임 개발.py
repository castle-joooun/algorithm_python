n, m = map(int, input().split())
x, y, arrow = map(int, input().split())
data = [list(map(int, input().split())) for i in range(n)]
visited = [[False] * (m + 1) for _ in range(n + 1)]

print(visited)

x, y = x - 1, y - 1

result = 1
count = 0
visited[x][y] = True

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

while True:
    xx = dx[arrow] + x
    yy = dy[arrow] + y

    if 0 <= xx < n and 0 <= yy < m and data[xx][yy] != 0 and visited[xx][yy] == False:
        result += 1
        x = xx
        y = yy
        count = 0
    else:
        arrow = 1 if arrow == 3 else arrow + 1

    count += 1

    if count == 4:
        break

print(result)
