def dfs(time, score, idx):
    global result
    if time > m:
        return
    if idx == n:
        result = max(result, score)
    else:
        dfs(time + d[idx][1], score + d[idx][0], idx + 1)
        dfs(time, score, idx + 1)


n, m = map(int, input().split())
d = []
for _ in range(n):
    d.append(tuple(map(int, input().split())))

result = 0
visited = [False] * n
dfs(0, 0, 0)
print(result)