# https://www.acmicpc.net/problem/13459
from collections import deque

n, m = map(int, input().split())
data = []
answer = 0
visited = set()
q = deque()

for _ in range(n):
    data.append(list(input()))

# 빨, 파, 구멍 찾기
rx = ry = bx = by = 0
for i in range(n):
    for j in range(m):
        if data[i][j] == 'R':
            rx, ry = i, j
        if data[i][j] == 'B':
            bx, by = i, j
q.append([rx, ry, bx, by, 1])
visited.add((rx, ry, bx, by))


def move(x, y, dx, dy):
    count = 0
    while data[x + dx][y + dy] != '#' and data[x][y] != 'O':
        x += dx
        y += dy
        count += 1
    return x, y, count


while q:
    cur_rx, cur_ry, cur_bx, cur_by, level = q.popleft()
    if level > 10:
        break

    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        next_rx, next_ry, r_count = move(cur_rx, cur_ry, dx, dy)
        next_bx, next_by, b_count = move(cur_bx, cur_by, dx, dy)

        # ✅ 두 구슬의 다음 위치가 이미 방문했던 위치라면, 다른 방향으로 기울이기를 시도한다.
        if (next_rx, next_ry, next_bx, next_by) in visited:
            continue
        # ✅ 파란 구슬의 다음 위치가 구멍이라면, 다른 방향으로 기울이기를 시도한다.
        if data[next_bx][next_by] == 'O':
            continue
        # ✅ 빨간 구슬의 다음 위치가 구멍이라면, 반복문을 종료한다.
        if data[next_rx][next_ry] == 'O':
            answer = 1
            break
        # ✅ 두 구슬의 다음 위치가 동일할 때, 이동 횟수가 더 많은 구슬의 위치를 한 칸 뒤로 이동한다.
        if next_rx == next_bx and next_ry == next_by:
            if r_count > b_count:
                next_rx -= dx
                next_ry -= dy
            else:
                next_bx -= dx
                next_by -= dy
        q.append([next_rx, next_ry, next_bx, next_by, level + 1])
        # ✅ 두 구슬의 다음 위치를 방문했다고 표시한다.
        visited.add((next_rx, next_ry, next_bx, next_by))
    else:
        continue
    break

print(answer)
