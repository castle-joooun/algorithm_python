def dfs(L, v):
    global cnt
    if L == k:
        if sum(result) % m == 0:
            cnt += 1
    else:
        for i in range(v, n):
            result[L] = d[i]
            dfs(L + 1, i + 1)


n, k = map(int, input().split())
d = list(map(int, input().split()))
m = int(input())

result = [0] * k
cnt = 0
dfs(0, 0)
print(cnt)