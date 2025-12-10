# https://www.acmicpc.net/problem/17142
from collections import deque
from itertools import combinations

n, m = map(int, input().split())
data = []
virus = []
result = 10 ** 8
arrows = [(1, 0), (0, 1), (-1, 0), (0, -1)]

# input 받음
for i in range(n):
    data.append(list(map(int, input().split())))

# 바이러스 확인
for r in range(n):
    for c in range(n):
        if data[r][c] == 2:
            virus.append((r, c))

combines = combinations(virus, m)


# 가능한 범위인지 확인
def possible_range(x, y):
    return 0 <= x < n and 0 <= y < n


# bfs 확인
def bfs(test_virus):
    queue = deque([list(test) + [0] for test in test_virus])
    new_map = [row[:] for row in data]
    visited = [[False] * n for _ in range(n)]

    # 활성 바이러스 위치 방문 처리
    for x, y in test_virus:
        visited[x][y] = True

    max_s = 0

    while queue:
        x, y, s = queue.popleft()

        for dx, dy in arrows:
            nx, ny = x + dx, y + dy
            if possible_range(nx, ny) and not visited[nx][ny]:
                # 빈 칸(0) 또는 비활성 바이러스(2)로 확산
                if new_map[nx][ny] == 0 or new_map[nx][ny] == 2:
                    visited[nx][ny] = True
                    queue.append([nx, ny, s + 1])

                    # 원래 빈 칸(0)이었을 때만 시간 갱신
                    if new_map[nx][ny] == 0:
                        new_map[nx][ny] = 2
                        max_s = s + 1

    # new_map에서 0이 없는지 확인
    no_zero = all(val != 0 for row in new_map for val in row)
    if no_zero:
        return max_s
    else:
        return 10 ** 8


for test_combine in combines:
    result = min(bfs(test_combine), result)

if result == 10 ** 8:
    print(-1)
else:
    print(result)
