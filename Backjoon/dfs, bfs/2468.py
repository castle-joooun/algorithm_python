"""
### 💡 풀이 순서

> 이문제도 처음에 이해가 힘들었다. 그림을 그려 차근히 살펴보니 3차원인 건물이었다. 아마 3차원 배열을 만들어서 관리를 해야할 것 같다.
>

### 🏭 알고리즘

> BFS
> BFS가 개인적으로 더 쉬워서 BFS로 진행하였다.
>

### ⚙️ 시간 복잡도 분석

> n^3이고 n은 최대 100이하니까 1억,
아슬아슬하긴 한데 통과는 될 것 같다.
>

### ‼️ 문제에서 중요한 부분

> 3차원 배열로 그래프와 방문 그래프를 나타내야 할 것 같다.
>
"""

import sys
from collections import deque

input = sys.stdin.readline

while True:
    l, r, c = map(int, input().split())

    if l == 0 and r == 0 and c == 0:
        break

    graph = []

    for f in range(l):
        for y in range(r):
            pass


    # minutes = 0

    # if bfs()


def bfs(start_node):
    queue = deque([])
    queue.append(start_node)

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while queue:
        y, x = queue.popleft()
        visited[y - 1][x - 1] = True

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 > nx >= n and 0 > ny >= n:
                continue

            if not visited[ny][nx] and graph[ny][nx] > water:
                queue.append((ny, nx))



