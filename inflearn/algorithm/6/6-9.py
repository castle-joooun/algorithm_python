from itertools import permutations


def dfs(start, L, d):
    global result
    if L == 1:
        if sum(d) == f:
            result.append(start)
    else:
        lt, rt = 0, 1
        check = []
        while len(check) < L:
            check.append(d[lt] + d[rt])
            lt += 1
            rt += 1
        dfs(start, L - 1, check)


n, f = map(int, input().split())

d = [i for i in range(1, n + 1)]
d = list(permutations(d, n))

result = []
for x in d:
    if len(result) == 0:
        dfs(x, n - 1, list(x))
    else:
        break

for x in result[0]:
    print(x, end=' ')
