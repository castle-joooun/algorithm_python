def dfs(idx, a, b, c):
    global step
    if idx == n:
        if a == b or b == c or a == c:
            return
        else:
            step = min(step, max(a, b, c) - min(a, b, c))
    else:
        for i in range(n):
            dfs(idx + 1, a + d[i], b, c)
            dfs(idx + 1, a, b + d[i], c)
            dfs(idx + 1, a, b, c + d[i])


n = int(input())
d = []
for _ in range(n):
    d.append(int(input()))

people = [0] * 3
step = 1e9
dfs(0, 0, 0, 0)
print(step)