from collections import deque

# 맵의 크기
n = int(input())
data = [[0] * (n + 2) for _ in range(n + 2)]
# 사과의 개수
k = int(input())
for _ in range(k):
    x, y = map(int, input().split())
    data[x][y] = 1
# 방향의 정보
l = int(input())
arrows = deque([list(input().split()) for _ in range(l)])

result = 0
arrow = 0

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

x = 1
y = 1
data[1][1] = 2

tails = deque([])

while True:
    if len(arrows) != 0 and int(arrows[0][0]) == result:
        check_arrow = arrows.popleft()[1]

        if check_arrow == 'L':
            arrow = 3 if arrow == 0 else arrow - 1
        else:
            arrow = 0 if arrow == 3 else arrow + 1

    nx = x + dx[arrow]
    ny = y + dy[arrow]

    if nx == 0 or ny == 0 or nx == n + 1 or ny == n + 1:
        print(result + 1)
        break
    # 이동 방향이 자기 몸이면 return
    if data[nx][ny] == 2:
        print(result + 1)
        break

    # 이동 방향이 사과가 아니라면 꼬리 땡겨오기
    # 사과라면 안 줄이기
    if data[nx][ny] != 1:
        if len(tails) != 0:
            tail_x, tail_y = tails.popleft()
            data[tail_x][tail_y] = 0
            tails.append([x, y])
        else:
            data[x][y] = 0
    else:
        tails.append([x, y])
    data[nx][ny] = 2

    x = nx
    y = ny

    result += 1
