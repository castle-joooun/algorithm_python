def dfs(idx, g):
    possible[abs(g)] = 0
    if idx == k:
        return
    else:
        dfs(idx + 1, g + d[idx])
        dfs(idx + 1, g - d[idx])
        dfs(idx + 1, g)


k = int(input())
d = list(map(int, input().split()))

possible = [1] * (sum(d) + 1)
dfs(0, 0)
print(sum(possible))