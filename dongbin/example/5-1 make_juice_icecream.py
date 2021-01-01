n, m = map(int, input().split())

ice_map = []
for i in range(n):
    ice_map.append(list(map(int, input())))


def ice(x, y):
    while True:
        if x <= -1 or x >= n or y <= -1 or y >= m:
            return False

        if ice_map[x][y] == 0:
            ice_map[x][y] = 1

            ice(x + 1, y)
            ice(x - 1, y)
            ice(x, y - 1)
            ice(x, y + 1)
            return True
        return False


result = 0
for i in range(n):
    for j in range(m):
        if ice(i, j):
            result += 1

print(result)