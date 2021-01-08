def dfs(idx, money):
    global cnt
    if money < 0:
        return
    if idx == k:
        if money == 0:
            cnt += 1
    else:
        for i in range(0, d[idx][1] + 1):
            dfs(idx + 1, money - (d[idx][0] * i))


t = int(input())
k = int(input())
d = []
for _ in range(k):
    d.append(tuple(map(int, input().split())))

cnt = 0
dfs(0, t)
print(cnt)