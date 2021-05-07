from collections import deque


def solution(board):
    answer = int(1e9)

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    q = deque([[0, 0], 0, 0, 0])

    while q:
        xy, c, a, k = q.popleft()
        x, y = xy

        if k * 100 + c * 500 > answer:
            continue

        if (x, y) == (len(board) - 1, len(board) - 1):
            answer = min(answer, k * 100 + c * 500)

        nx = x + dx[a]
        ny = y + dy[a]

        if 0 > nx or nx >= len(board) or 0 > ny or ny >= len(board) or board[nx][ny] == 1:
            ra = a + 1 if a != 3 else 0
            la = a - 1 if a != 0 else 3
            c += 1

            q.append([[nx, ny], c, ra, k])
            q.append([[nx, ny], c, la, k])
        else:
            x, y = nx, ny
            k += 1

            q.append([[x, y], c, a, k])

    return answer


print(solution([[0, 0, 0], [0, 0, 0], [0, 0, 0]]))
