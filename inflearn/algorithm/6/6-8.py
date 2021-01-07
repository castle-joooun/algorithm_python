def dfs(L, list_):
    global cnt

    if L == m:
        cnt += 1
        for x in list_:
            print(x, end=' ')
        print()
    else:
        for i in range(1, n + 1):
            if i not in list_:
                dfs(L + 1, list_ + [i])


n, m = map(int, input().split())

check = [0] * (n + 1)
cnt = 0

dfs(0, [])
print(cnt)