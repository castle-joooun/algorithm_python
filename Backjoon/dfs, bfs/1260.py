from collections import deque
import sys
input = sys.stdin.readline


def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


'''
def dfs(graph, v):
    visited = []
    stack = graph[v]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            stack.extend(graph[node])
    return stack
'''


def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


n, m, v = map(int, input().split())
d = [set() for _ in range(n + 1)]
for i in range(1, n + 1):
    a, b = map(int, input().split())
    d[a].add(b)
    d[b].add(a)

for x in d:
    print(x)

visited_dfs = [False] * (m + 1)
visited_bfs = [False] * (m + 1)

dfs(d, v, visited_dfs)
print()
bfs(d, v, visited_bfs)
