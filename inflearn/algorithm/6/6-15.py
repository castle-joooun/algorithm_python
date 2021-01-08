def dfs(v, check):
    global cnt
    if check[n] == 1:
        cnt += 1
    else:
        for i in range(1, n + 1):
            if d[v][i] != 0 and check[i] == 0:
                check[i] = 1
                dfs(i, check)
                check[i] = 0


n, m = map(int, input().split())
d = [[0] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    d[a][b] = 1

cnt = 0
check = [0] * (n + 1)
check[1] = 1
dfs(1, check)
print(cnt)