import sys
input = sys.stdin.readline


def bfs(d, node, visited):
    if visited[node] == check:
        return True
    elif visited[node] == -1:
        visited[node] = check
        bfs(d, d[node], visited)
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
        node = d[i]
        if bfs(d, node, visited):
            cnt += 1
            check += 1

    print(cnt)