n, m = map(int, input().split())
d = [[0] * (n + 1) for i in range(n + 1)]
for i in range(m):
    a, b, c = map(int, input().split())
    d[a][b] = c

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(d[i][j], end=' ')
    print()