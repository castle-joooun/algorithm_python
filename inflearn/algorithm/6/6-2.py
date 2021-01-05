def dfs_front(d, n):
    print(n, end=' ')
    check = d[n]
    visited[n] = True
    for x in check:
        if not visited[x]:
            dfs_front(d, x)


def dfs_mid(d, n):
    check = d[n]
    visited[n] = True
    for x in check:
        if len(check) == 1:
            stack.append(x)
        if not visited[x]:
            dfs_mid(d, x)
        else:
            if x not in stack:
                stack.append(x)


def dfs_mid_solv(n):
    if n > 7:
        return
    else:
        dfs_mid_solv(n * 2)
        print(n)
        dfs_mid_solv(n * 2 + 1)


def dfs_back(d, n):
    visited[n] = True
    check = d[n]
    for x in check:
        if not visited[x]:
            dfs_back(d, x)
    else:
        print(n, end=' ')


d = [[], [2, 3], [1, 4, 5], [1, 6, 7], [2], [2], [3], [3]]

visited = [False] * (len(d) + 1)
dfs_front(d, 1)
print()

stack = []
visited = [False] * (len(d) + 1)
dfs_mid(d, 1)
for x in stack:
    print(x, end=' ')
print()

visited = [False] * (len(d) + 1)
dfs_back(d, 1)