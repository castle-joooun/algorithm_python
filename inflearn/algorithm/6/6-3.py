def dfs(v):
    if v == n + 1:
        for i in range(1, n + 1):
            if check[i] == 1:
                print(i, end=' ')
        else:
            print()
    else:
        check[v] = 1
        dfs(v + 1)
        check[v] = 0
        dfs(v + 1)


n = int(input())
check = [0] * (n + 1)
dfs(1)