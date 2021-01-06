import sys
input = sys.stdin.readline


def dfs(v, sum, tsum):
    global result
    if sum + (total - tsum) < result:
        return
    if sum > c:
        return
    if v == n:
        result = max(result, sum)
    else:
        dfs(v + 1, sum + d[v], tsum + d[v])
        dfs(v + 1, sum, tsum + d[v])


c, n = map(int, input().split())
d = []

for _ in range(n):
    d.append(int(input()))

result = 0
total = sum(d)
dfs(0, 0, 0)
print(result)