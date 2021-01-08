from collections import deque


def bfs():
    global good, day

    queue = deque(good)
    new_good = []
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if d[nx][ny] == 0:
                    d[nx][ny] = 1
                    new_good.append((nx, ny))
    good = new_good


n, m = map(int, input().split())
d = []
good = []
for i in range(m):
    d.append(list(map(int, input().split())))
    for j in range(n):
        if d[i][j] == 1:
            good.append((i, j))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

day = 0
idx = 0
while idx != m:
    while 0 in d[idx]:
        day += 1
        bfs()
    idx += 1

print(day)