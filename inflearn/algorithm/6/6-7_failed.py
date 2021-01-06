def dfs(i, cnt, money):
    global result
    if cnt > result:
        return
    if i == n:
        if money == 0:
            result = min(result, cnt)
        return
    else:
        if i < n + 1:
            if check[i] == 1:
                cnt += (money //d[i])
                money %= d[i]

            check[i + 1] = 1
            dfs(i + 1, cnt, money)
            check[i + 1] = 0
            dfs(i + 1, cnt, money)
        else:
            dfs(i + 1, cnt, money)


n = int(input())
d = list(map(int, input().split()))
m = int(input())
d.sort(reverse=True)

check = [0] * n
result = 1e9

check[0] = 1
dfs(0, 0, m)
check[0] = 0
dfs(0, 0, m)

print(result)