n, m = map(int, input().split())
data = [int(input()) for _ in range(n)]

d = [10001] * (m + 1)

for i in range(1, m):
    for x in data:
        if x * i <= m:
            d[x * i] = min(d[x * i], i)

    for x in data:
        if d[i] != 10001 and i + x <= m:
            d[x + i] = min(d[x] + d[i], d[x + i])

if d[m] != 10001:
    print(d[m])
else:
    print(-1)
