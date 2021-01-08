from sys import stdin
import sys
sys.setrecursionlimit(3000)


def dfs(a, b):
    global nums
    if visited[a][b]:
        pass
    else:
        visited[a][b] = True
        if d[a][b] == 1:
            nums += 1
        for i in range(8):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < h and 0 <= ny < w:
                if not visited[nx][ny] and d[nx][ny] == 1:
                    dfs(nx, ny)


while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    d = [[0] * w for _ in range(h)]
    for i in range(h):
        line = stdin.readline().split()
        for j, b in enumerate(line):
            d[i][j] = int(b)

    # 12시부터 시계방향으로 이동하는 x, y값
    dx = [0, 1, 1, 1, 0, -1, -1, -1]
    dy = [-1, -1, 0, 1, 1, 1, 0, -1]

    nums = 0
    island = []
    visited = [[False] * w for _ in range(h)]

    for a in range(h):
        for b in range(w):
            dfs(a, b)
            if nums != 0:
                island.append(nums)
            nums = 0

    print(len(island))