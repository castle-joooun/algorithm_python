def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])
    # return x
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


# node, edge
v, e = map(int, input().split())
parent = [0] * (v + 1)

# parent initialize is self value in parent table
for i in range(1, v + 1):
    parent[i] = i

# start union
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

for i in range(1, v + 1):
    print(find_parent(parent, i), end=' ')

print()

for i in range(1, v + 1):
    print(parent[i], end=' ')

