k = int(input())
for _ in range(k):
    n = int(input())
    d = [list(map(int, input().split())) for _ in range(2)]

    d[0][1] += d[1][0]
    d[1][1] += d[0][0]

    for i in range(2, n):
        d[0][i] += max(d[1][i - 1], d[1][i - 2])
        d[1][i] += max(d[0][i - 1], d[0][i - 2])

    print(max(d[0][n - 1], d[1][n - 1]))
