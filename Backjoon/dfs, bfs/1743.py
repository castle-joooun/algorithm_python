"""
### 💡 풀이 순서
> 일단 문제를 이해하기 위해 종이위에 그려보았다.
그래프를 그린 뒤 접근하는것이 중요할듯

그려보니 대각선으로 접하지 않은 좌표들 중 가장 큰 값을 갱신하는 방향을 잡았다. DFS/BFS를 이용하여 접근하면 좋을 듯 하다.

각각의 좌표에 접근할때는 방문 여부를 정하자
>

### 🏭 알고리즘
> BFS
> DFS보다 개인적으로 구현하기 쉽고 넓이 탐색이라 더 좋지 않을까 했다
>

### ⚙️ 시간 복잡도 분석
>
>

### ‼️ 문제에서 중요한 부분
> 방문여부를 체크해가면서 최대값을 갱신해 가는것
>
"""

import sys
from collections import deque

input = sys.stdin.readline

n, m, k = map(int, input().split())
visited = [[False] * m for _ in range(n)]
graph = \
    [tuple(map(int, input().split())) for _ in range(k)]

max_num = 1


def bfs(start_node):
    queue = deque([])
    queue.append(start_node)

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    count = 0

    while queue:
        y, x = queue.popleft()
        visited[y-1][x-1] = True

        count += 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not visited[ny][nx]:
                queue.append((ny, nx))

    return count


for y, x in graph:
    if visited[y-1][x-1]:
        continue

    max_num = max(max_num, bfs((y, x)))

print(max_num)
