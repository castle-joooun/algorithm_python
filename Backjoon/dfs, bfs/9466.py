from collections import deque
import sys
input = sys.stdin.readline


def bfs(i):
    queue = deque([i])
    check = [i]

    while queue:
        next = d[queue.popleft()]

        if visited[next] == 0:
            queue.append(next)
            check.append(next)
            visited[next] = team
        elif visited[next] == team:
            if next in check:
                if check[-1] == next:
                    return len(check) - 1
                else:
                    queue.append(next)
                    check.remove(next)
        else:
            return 0


t = int(input())

for _ in range(t):
    n = int(input())
    d = [0] + list(map(int, input().split()))

    visited = [0] * (n + 1)
    team = 1
    result = 0

    for i in range(1, n + 1):
        result += bfs(i)
        team += 1

    print(result)