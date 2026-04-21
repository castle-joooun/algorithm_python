n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())

# Please write your code here.
x, y = r - 1, c - 1
for i in range(grid[x][y]):
    for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        nx, ny = dx * i + x, dy * i + y
        if 0 <= nx < n and 0 <= ny < n:
            grid[nx][ny] = 0

for j in range(n):
    temp = [0 for _ in range(n)]
    for i in range(n):
        if grid[i][j] != 0:
            temp.append(grid[i][j])
    temp = temp[-n:]
    for i in range(n):
        grid[i][j] = temp[i]

for x in grid:
    print(' '.join(str(i) for i in x))



