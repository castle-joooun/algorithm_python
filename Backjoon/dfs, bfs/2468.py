"""
### 💡 풀이 순서

> 처음에 문제를 이해하기 어려웠다. 어디서도 내린 비의 양을 알려주지 않았기 떄문이다. 다시 한번 살펴보니 최소값부터 최대값을 둘러보며 최대 안전지대를 찾는거였다.
>

### 🏭 알고리즘

> BFS
> BFS가 개인적으로 더 쉬워서 BFS로 진행하였다.
>

### ⚙️ 시간 복잡도 분석

> 위에서 설명..!
>

### ‼️ 문제에서 중요한 부분

> 문제에서 물의 양을 늘려가며 조사할때 방문 그래프를 초기화시켜줘야 한다.
>
"""

import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

max_count = 0


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


for water in range(max(map(max, graph))):
    count = 0
    visited = [[False] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if not visited:
                bfs((i, j))
                count += 1

    max_count = max(max_count, count)

print(max_count)
