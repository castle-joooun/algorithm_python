def dfs(x, y):
    if x <= -1 or x > m or y <= -1 or y > n:
        return False

    print(x, y)
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False


n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j):
            result += 1

print(result)
