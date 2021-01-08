def dfs(L, i):
    global cnt
    if L == m:
        for j in range(m):
            print(result[j], end=' ')
        print()
        cnt += 1
    else:
        for k in range(i, n + 1):
            result[L] = k
            dfs(L + 1, k + 1)


n, m = map(int, input().split())
result = [0] * m
cnt = 0
dfs(0, 1)
print(cnt)
