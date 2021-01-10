import sys
from collections import deque
input = sys.stdin.readline


def bfs_check_land(x, y, mark):
    queue = deque([(x, y)])

    while queue:
        x, y = queue.popleft()
        new_map[x][y] = mark

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < n:
                if d[nx][ny] == 1 and new_map[nx][ny] == 0:
                    queue.append((nx, ny))


def bfs_bridge(k, value):
    global result
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if d[nx][ny] == 1 and new_map[nx][ny] != k:
                    result = min(result, value)
                if d[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    value += 1
                    q.append((nx, ny))



n = int(input())
d = []
for _ in range(n):
    d.append(list(map(int, input().split())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
new_map = [[0] * n for _ in range(n)]
mark = 1

for i in range(n):
    for j in range(n):
        if d[i][j] == 1 and new_map[i][j] == 0:
            bfs_check_land(i, j, mark)
            mark += 1

result = 1e9
for k in range(1, mark):
    q = deque()
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if d[i][j] == 1 and new_map[i][j] == k:
                q.append((i, j))
    bfs_bridge(k, 0)

print(result)