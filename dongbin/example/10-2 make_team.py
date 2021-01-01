# number, computation
n, m = map(int, input().split())
team = [0] * (n + 1)


def find_parent(parent, x):
    if parent[x] != x:
        find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


for i in range(1, n + 1):
    team[i] = i

for _ in range(m):
    cal, a, b = map(int, input().split())

    if cal == 0:
        union_parent(team, a, b)
    if cal == 1:
        if find_parent(team, a) == find_parent(team, b):
            print('YES')
        else:
            print('NO')