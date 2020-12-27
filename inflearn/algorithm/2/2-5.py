n, m = map(int, input().split())
d = [0 for _ in range(n + m + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        idx = i + j
        d[idx] += 1

max_num = max(d)
for i in range(n + m + 1):
    if max_num == d[i]:
        print(i, end=' ')