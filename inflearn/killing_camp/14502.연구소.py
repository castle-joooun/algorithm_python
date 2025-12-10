# https://www.acmicpc.net/problem/14502
from collections import deque
from itertools import combinations
import copy

# 입력받기
n, m = map(int, input().split())
data = []

for _ in range(n):
    data.append(list(map(int, input().split())))

# 빈 공간인 곳을 조합으로 선정
combines = list(combinations([
    (i, j) for i in range(n) for j in range(m)
    if data[i][j] == 0
], 3))
# 방향 설정
arrows = [(0, 1), (1, 0), (0, -1), (-1, 0)]
result = 0

# 바이러스 공간 체크
virus = []
for r in range(len(data)):
    for c in range(len(data[0])):
        if data[r][c] == 2:
            virus.append((r, c))


# 범위 안인 것 체크
def possible(x, y):
    return 0 <= x < n and 0 <= y < m


# 빈 공간 체크
def cal_empty(new_map):
    count = 0
    for row in new_map:
        count += row.count(0)
    return count


# 바이러스 확산
def bfs(new_map):
    queue = deque(virus[::])

    while queue:
        x, y = queue.popleft()
        for dx, dy in arrows:
            nx, ny = x + dx, y + dy
            if possible(nx, ny) and new_map[nx][ny] == 0:
                queue.append((nx, ny))
                new_map[nx][ny] = 2

    return cal_empty(new_map)


for test_combines in combines:
    # data에 +
    for r, c in test_combines:
        data[r][c] = 1
    new_map = copy.deepcopy(data)
    # 실행
    result = max(bfs(new_map), result)
    # 초기화
    for r, c in test_combines:
        data[r][c] = 0

print(result)
