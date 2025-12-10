# https://leetcode.com/problems/shortest-path-in-binary-matrix/description/
from typing import List
from collections import deque


def shortestPathBinaryMatrix(grid: List[List[int]]) -> int:
    if grid[0][0] == 1:
        return -1

    # bfs
    n = len(grid)
    visited = [[False for _ in range(n)] for _ in range(n)]
    arrows = [(0, 1), (1, 0), (0, -1), (-1, 0),
              (1, 1), (-1, 1), (1, -1), (-1, -1)]
    queue = deque([(0, 0, 1)])
    visited[0][0] = True

    while queue:
        x, y, d = queue.popleft()

        if x == n -1 and y == n -1:
            return d

        for dx, dy in arrows:
            nx, ny = dx + x, dy + y
            if 0 <= nx < n and 0 <= ny < n and \
                    not visited[nx][ny] and grid[nx][ny] == 0:
                queue.append((nx, ny, d + 1))
                visited[nx][ny] = True

    return -1


print(shortestPathBinaryMatrix(
    [[0,1],[1,1]]
))
