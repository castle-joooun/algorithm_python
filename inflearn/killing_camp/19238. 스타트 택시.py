# https://www.acmicpc.net/problem/19238
from collections import deque

n, m, fuel = map(int, input().split())
data = []
for i in range(n):
    data.append(list(map(int, input().split())))
tx, ty = map(int, input().split())
tx -= 1
ty -= 1

passengers = []
for _ in range(m):
    px, py, gx, gy = map(int, input().split())
    passengers.append(((px - 1, py - 1), (gx - 1, gy - 1)))

completed = [False] * m


# 가장 가까운 승객 찾기
def find_nearest_passenger(sx, sy):
    # 시작 위치에 승객이 있는지 체크
    for i in range(m):
        if passengers[i][0] == (sx, sy) and not completed[i]:
            return i, 0

    visited_bfs = [[False] * n for _ in range(n)]
    queue = deque([(sx, sy, 0)])
    visited_bfs[sx][sy] = True
    candidates = []
    min_dist = float('inf')

    while queue:
        x, y, dist = queue.popleft()

        # 이미 더 가까운 승객을 찾았으면 종료
        if dist > min_dist:
            break

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy

            if 0 <= nx < n and 0 <= ny < n and not visited_bfs[nx][ny] and \
                    data[nx][ny] == 0:
                visited_bfs[nx][ny] = True

                # 승객 발견
                for i in range(m):
                    if passengers[i][0] == (nx, ny) and not completed[i]:
                        candidates.append((nx, ny, dist + 1, i))
                        min_dist = min(min_dist, dist + 1)
                        break

                queue.append((nx, ny, dist + 1))

    if not candidates:
        return -1, -1

    # 거리, 행, 열 순으로 정렬
    candidates.sort(key=lambda x: (x[2], x[0], x[1]))
    return candidates[0][3], candidates[0][2]


# 목적지까지 거리 찾기
def find_distance_to_goal(sx, sy, gx, gy):
    if (sx, sy) == (gx, gy):
        return 0

    visited_bfs = [[False] * n for _ in range(n)]
    queue = deque([(sx, sy, 0)])
    visited_bfs[sx][sy] = True

    while queue:
        x, y, dist = queue.popleft()

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy

            if 0 <= nx < n and 0 <= ny < n and not visited_bfs[nx][ny] and \
                    data[nx][ny] == 0:
                if (nx, ny) == (gx, gy):
                    return dist + 1

                visited_bfs[nx][ny] = True
                queue.append((nx, ny, dist + 1))

    return -1


# 메인 로직
for _ in range(m):
    # 1. 가장 가까운 승객 찾기
    passenger_idx, dist_to_passenger = find_nearest_passenger(tx, ty)

    if passenger_idx == -1 or fuel < dist_to_passenger:
        print(-1)
        exit()

    fuel -= dist_to_passenger
    tx, ty = passengers[passenger_idx][0]

    # 2. 목적지까지 이동
    gx, gy = passengers[passenger_idx][1]
    dist_to_goal = find_distance_to_goal(tx, ty, gx, gy)

    if dist_to_goal == -1 or fuel < dist_to_goal:
        print(-1)
        exit()

    fuel -= dist_to_goal
    fuel += dist_to_goal * 2  # ✅ 해당 거리의 2배 충전
    tx, ty = gx, gy
    completed[passenger_idx] = True

print(fuel)
