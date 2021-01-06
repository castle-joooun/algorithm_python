import sys


def dfs(v, sum):
    if sum > total // 2:
        return
    if v == n:
        if sum == (total - sum):
            print('YES')
            sys.exit(0)
    else:
        dfs(v + 1, sum + d[v])
        dfs(v + 1, sum)


n = int(input())
d = list(map(int, input().split()))
total = sum(d)
dfs(0, 0)
print('NO')