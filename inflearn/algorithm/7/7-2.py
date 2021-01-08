def dfs(idx, money):
    global amount
    if idx > n:
        return
    if idx == n:
        amount = max(amount, money)
    else:
        dfs(idx + d[idx][0], money + d[idx][1])
        dfs(idx + 1, money)


n = int(input())
d = []
for _ in range(n):
    d.append(tuple(map(int, input().split())))

amount = 0
dfs(0, 0)
print(amount)