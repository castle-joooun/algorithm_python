"""
### 💡 풀이 순서

> 연속되어 연결된 숫자들을 찾아 카운트하고 단지수도 늘려가면 될 것  같다.
>

### 🏭 알고리즘

> BFS
> DFS보다 개인적으로 구현하기 쉽고 넓이 탐색이라 더 좋지 않을까 했다
>

### ⚙️ 시간 복잡도 분석

> n^2 + 4n 정도가 나오는데 최대 n이 100, m이 100이니
10000까지 나올 수 있다.

10000^2은 1억이므로 통과할거싱라 생각한다.
>

### ‼️ 문제에서 중요한 부분

> 방문여부를 체크해가면서 단지수를 세고, 단지가 끝나면 append하여 리스트로 나타내기 or 바로 print로 출력하기
>
"""

import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
normal_count = 0
color_count = 0

normal_visited = [[False] * n for _ in range(n)]
color_visited = [[False] * n for _ in range(n)]

graph = [list(input()) for _ in range(n)]


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


for x1, y1, x2, y2 in graph:
    for i in range(y1 - y2):
        for j in range(x1 - x2):
            visited[i][j] = True

for y in range(n):
    for x in range(m):
        if not visited[y][x]:
            num_list.append(bfs((y, x)))

print(len(num_list))
for x in num_list:
    print(x)
