# https://leetcode.com/problems/number-of-islands/
from typing import List
from collections import deque


def numIslands(grid: List[List[str]]) -> int:
    n = len(grid)
    m = len(grid[0])
    visited = [[False for _ in range(m)] for _ in range(n)]

    count = 0

    def find_land(c, r):
        visited[c][r] = True

        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = dx + c, dy + r
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] \
                    and grid[nx][ny] == "1":
                find_land(nx, ny)

    for c in range(n):
        for r in range(m):
            if not visited[c][r] and grid[c][r] == "1":
                count += 1
                find_land(c, r)

    return count


print(numIslands(
    [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
))
