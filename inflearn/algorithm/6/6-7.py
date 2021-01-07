def dfs(i, cnt, money):
    global result
    if cnt >= result or (i == n and money > 0):
        return
    if i == n:
        if money == 0:
            result = min(result, cnt)
    else:
        dfs(i + 1, cnt + (money // d[i]), money % d[i])
        dfs(i + 1, cnt, money)


n = int(input())
d = list(map(int, input().split()))
m = int(input())
d.sort(reverse=True)

result = 1e9
dfs(0, 0, m)

print(result)