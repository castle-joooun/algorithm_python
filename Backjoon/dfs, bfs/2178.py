from collections import deque


def dfs(x, y, cnt):
    global step
    if cnt > step:
        return
    if x == n - 1 and y == m - 1:
        step = min(step, cnt)
    else:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny] and d[nx][ny] == 1:
                    visited[nx][ny] = True
                    dfs(nx, ny, cnt + 1)
                    visited[nx][ny] = False

'''
def bfs(cnt):
    global step
    visited[0][0] = True
    queue = deque([(0, 0)])
    check = -1
    while queue:
        if check > 0:
            cnt -= check
        check = -1
        x, y = queue.popleft()
        if x == n - 1 and y == m - 1:
            step = cnt
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny] and d[nx][ny] == 1:
                    visited[nx][ny] = True
                    cnt += 1
                    check += 1
                    queue.append((nx, ny))
'''


n, m = map(int, input().split())
d = []
for _ in range(n):
    d.append(list(map(int, input())))

step = 1e9
visited = [[False] * m for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
#'''
visited[0][0] = True
dfs(0, 0, 1)
#'''
'''
bfs(1)
'''
print(step)
