def dfs(i, j):
    global cnt, result

    visited[i][j] = True
    check = False
    for k in range(4):
        if d[i + dx[k]][j + dy[k]] != 0 and not visited[i + dx[k]][j + dy[k]]:
            check = True
            break
    else:
        print(cnt)
        cnt = 0
        result += 1
        j += 1
        if j == n + 2:
            i += 1
        dfs(i, j)

    if check:
        for k in range(4):
            if d[i + dx[k]][j + dy[k]] != 0 and not visited[i + dx[k]][j + dy[k]]:
                cnt += 1
                dfs(i + dx[k], j + dy[k])


n = int(input())
d = [[0] * (n + 2)]
for _ in range(n):
    d.append([0] + list(map(int, input())) + [0])
d.append([0] * (n + 2))

visited = [[False] * (n + 2) for _ in range(n + 2)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
cnt = 1 if d[1][1] == 1 else 0
result = 0
dfs(1, 1)