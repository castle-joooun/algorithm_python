from collections import deque


# 이동 가능한 경우의 수 확인 함수
def get_next_pos(pos, new_board):
    next_pos = []
    lx, ly, rx, ry = pos[0][0], pos[0][1], pos[1][0], pos[1][1]
    # ✅ 상하좌우 이동이 가능한 경우를 구한다.
    for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
        nlx, nly, nrx, nry = lx + dx, ly + dy, rx + dx, ry + dy
        if new_board[nlx][nly] == 0 and new_board[nrx][nry] == 0:
            next_pos.append([(nlx, nly), (nrx, nry)])
    # ✅ 가로 방향일 경우 회전 가능한 경우를 구한다.
    if lx == rx:
        for i in [1, -1]:
            if new_board[lx + i][ly] == 0 and new_board[rx + i][ry] == 0:
                next_pos.append([(lx, ly), (lx + i, ly)])
                next_pos.append([(rx, ry), (rx + i, ry)])
            # ✅ 세로 방향일 경우 회전 가능한 경우를 구한다.
    if ly == ry:
        for i in [1, -1]:
            if new_board[lx][ly + i] == 0 and new_board[rx][ry + i] == 0:
                next_pos.append([(lx, ly), (lx, ly + i)])
                next_pos.append([(rx, ry), (rx, ry + i)])
    return next_pos


def solution(board):
    n = len(board)
    # ✅ 인덱싱의 편의를 위해 원본 배열에 상하좌우로 한 칸씩 늘린 새 배열을 만든다.
    new_board = [[1 for _ in range(n + 2)] for _ in range(n + 2)]
    # ✅ 배열의 모서리 부분을 1로 채우고 내부를 원본 배열의 값들로 채운다.
    for i in range(n):
        for j in range(n):
            new_board[i + 1][j + 1] = board[i][j]
    # ✅ 로봇의 첫 위치를 방문표시하고 큐에 추가한다.
    robot_pos = [(1, 1), (1, 2)]
    q = deque()
    q.append((robot_pos, 0))
    visited = set()
    # 로봇의 위치는 set 자료형이지만 set은 hash할수 없는 함수이기에 set에 추가 불가. frozenset을 통해 hash가능하도록 변경
    visited.add(frozenset(robot_pos))
    # ✅ 큐가 빌때까지 반복한다.
    while q:
        cur_pos, cost = q.popleft()
        # ✅ 목적지에 도착한 경우 종료한다.

        if (n, n) in cur_pos:
            return cost
        # ✅ 현재 상태에서 이동가능한 상태를 구한다.
        for next_pos in get_next_pos(cur_pos, new_board):
            # ✅ 아직 방문하지 않았다면 방문한다.
            if frozenset(next_pos) not in visited:
                q.append((next_pos, cost + 1))
                visited.add(frozenset(next_pos))
    return -1
