def dfs(L, d):
    if len(d) != n and 1 in d:
        return
    if len(set(d)) == n:
        result.append(tuple(d))
    else:
        for i in range(1, d[0]):
            check = []
            idx = 0
            check.append(i)
            check.append(minus(d[0] - i))
            while len(check) < L:
                idx += 1
                check.append(minus(d[idx] - check[-1]))
            if -1 not in check:
                dfs(L + 1, check)


def minus(oper):
    if oper > 0:
        return oper
    return -1


n, f = map(int, input().split())
result = []
dfs(2, [16])

result.sort()
for x in result[0]:
    print(x, end=' ')