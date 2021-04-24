n, m = map(int, input().split())

d = [[False] * m for _ in range(n)]
x, y, arrow = map(int, input().split())
d[x][y] = True

array = []
for i in range(n):
    array.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def turn_left():
    global arrow
    arrow -= 1
    if arrow == -1:
        arrow = 3


count = 1
turn_time = 0
while True:
    turn_left()
    nx = x + dx[arrow]
    ny = y + dy[arrow]

    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        y = ny
        x = nx
        count += 1
        turn_time = 0
        continue
    else:
        turn_time += 1

    if turn_time == 4:
        nx = x - dx[arrow]
        ny = y - dy[arrow]

        if array[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0

print(count)
