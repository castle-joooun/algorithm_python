def check_mountain(a, b):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    for i in range(4):
        x = a + dx[i]
        y = b + dy[i]
        if d[a][b] <= d[x][y]:
            return False
    else:
        return True


n = int(input())
in_d = [list(map(int, input().split())) for _ in range(n)]
d = []

for i in range(n + 2):
    if i == 0 or i == n + 1:
        d.append([0] * (n + 2))
    else:
        d.append([0] + in_d[i - 1] + [0])

cnt = 0
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if check_mountain(i, j):
            cnt += 1
print(cnt)