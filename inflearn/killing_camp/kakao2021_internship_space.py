# https://school.programmers.co.kr/learn/courses/30/lessons/81302
from collections import deque


def is_blocked(board, r1, c1, r2, c2):
    """두 사람 사이에 파티션으로 막혀있는지 확인"""
    # 상하로 2칸 차이
    if r1 == r2 and abs(c1 - c2) == 2:
        mid_c = (c1 + c2) // 2
        return board[r1][mid_c] == 'X'

    # 좌우로 2칸 차이
    if c1 == c2 and abs(r1 - r2) == 2:
        mid_r = (r1 + r2) // 2
        return board[mid_r][c1] == 'X'

    # 대각선 (1,1): 두 경로 모두 막혀있어야 함
    if abs(r1 - r2) == 1 and abs(c1 - c2) == 1:
        # 두 경로 중 하나라도 뚫려있으면 거리두기 실패
        return board[r1][c2] == 'X' and board[r2][c1] == 'X'

    return True


def bfs(board):
    # P의 자리 기록
    people = deque()
    for i in range(5):
        for j in range(5):
            if board[i][j] == 'P':
                people.append((i, j))

    for i in range(len(people)):
        for j in range(i + 1, len(people)):
            r1, c1 = people[i]
            r2, c2 = people[j]

            manhattan = abs(r1 - r2) + abs(c1 - c2)
            # 맨해튼 거리 1: 바로 옆
            if manhattan == 1:
                return 0
            # 맨해튼 거리 2: 파티션 확인
            if manhattan == 2:
                if not is_blocked(board, r1, c1, r2, c2):
                    return 0
    return 1


def solution(places):
    answer = []

    for board in places:
        answer.append(bfs(board))

    return answer


# result = [1, 0, 1, 1, 1]
print(solution([
    ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
    ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
    ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
    ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
    ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
))
