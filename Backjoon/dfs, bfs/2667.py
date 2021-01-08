from collections import deque

n = int(input())
d = []
for _ in range(n):
    d.append(list(map(int, input())))


# 합쳐보기!!!
data = [[]]
for i in range(1, n + 1):
    data.append([])
    for j in range(1, n + 1):
        if d[i - 1][j - 1] == 1:
            data[i].append(j)

for x in data:
    print(x)
