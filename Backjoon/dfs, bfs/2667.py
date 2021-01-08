from sys import stdin


def dfs(x, y, cnt):
    visited[x][y] = True
    global nums
    if d[x][y] == 1:
        nums += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if not visited[nx][ny] and d[nx][ny] == 1:
                dfs(nx, ny, cnt)


n = int(input())
d = [[0] * n for _ in range(n)]
visited = [[False] * n for _ in range(n)]

for i in range(n):
    line = stdin.readline().strip()
    for j, b in enumerate(line):
        d[i][j] = int(b)

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
nums = 0
cnt = 1
numlist = []
for a in range(n):
    for b in range(n):
        if d[a][b] == 1 and not visited[a][b]:
            dfs(a, b, cnt)
            numlist.append(nums)
            nums = 0

print(len(numlist))
for x in sorted(numlist):
    print(x)
