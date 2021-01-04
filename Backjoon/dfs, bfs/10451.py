from collections import deque
import sys
input = sys.stdin.readline


def bfs(visited, node):
    queue = deque([node])

    while queue:
        next = d[queue.popleft()]
        if visited[next] == check:
            return True
        elif visited[next] == -1:
            visited[next] = check
            queue.append(next)
        else:
            return False


t = int(input())

for _ in range(t):
    n = int(input())
    d = list(map(int, input().split()))
    d.insert(0, [])
    visited = [-1] * (n + 1)

    cnt = 0
    check = 0

    for i in range(1, n + 1):
        if bfs(visited, i):
            cnt += 1
            check += 1

    print(cnt)