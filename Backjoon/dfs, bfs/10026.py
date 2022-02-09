"""
### 💡 풀이 순서

> 처음에 딱 든 생각은 visited를 2개로 나누어 정상인과 색약인의 경우를 둘다 거치려 했다. 근데 이렇게 되었을때 시간적으로 낭비가 분명히 날 것 이기때문에 비효율적인 코드가 될 수 밖에 없다.

시간제한은 1초이고 1억번 연산이 가능하다고 가정했을때
n은 100이고 최대 n^3이라면 100만이고,
이것을 2번 연산하면 200만이기 때문에 브루트 탐색 + BFS/DFS로 충분히 풀 수 있지 않을까 생각했다.

가능하면 한번 연산으로 가능하게 짜봐야겠다.
>

### 🏭 알고리즘

> BFS
> BFS가 개인적으로 더 쉬워서 BFS로 진행하였다.
>

### ⚙️ 시간 복잡도 분석

> 위에서 설명..!
코드를 완성한뒤에 다시 설명을 이어나가겠다.
>

### ‼️ 문제에서 중요한 부분

> 정상인과 색약인의 카운트를 잘 하기
>
"""

import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
color_visited = normal_visited = \
    [[False] * n for _ in range(n)]
graph = [list(input()) for _ in range(n)]

color_count = 0
normal_count = 0


def bfs(start_node, visited, search_type):
    queue = deque([])
    queue.append(start_node)

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    color = graph[start_node[0], start_node[1]]

    while queue:
        y, x = queue.popleft()
        visited[y - 1][x - 1] = True

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not visited[ny][nx]:
                if search_type == 'color' and color in ['R', 'G'] and \
                        graph[ny][nx] in ['R', 'G']:
                    queue.append((ny, nx))
                elif search_type == 'normal' and color == graph[ny][nx]:
                    queue.append((ny, nx))


for i in range(n):
    for j in range(n):
        if not color_visited[i][j]:
            color_count += 1
            bfs((j, i), color_visited, 'color')
        elif not normal_visited[i][j]:
            normal_count += 1
            bfs((j, i), color_visited, 'normal')

print(normal_count, color_count)
