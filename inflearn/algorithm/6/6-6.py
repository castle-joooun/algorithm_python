def dfs(L):
    global cnt
    if L == m:
        for j in range(m):
            print(check[j], end=' ')
        print()
        cnt = cnt + 1
    else:
        for i in range(1, n + 1):
            check[L] = i
            dfs(L + 1)


n, m = map(int, input().split())
check = [0] * (n + 1)
cnt = 0
dfs(0)
print(cnt)