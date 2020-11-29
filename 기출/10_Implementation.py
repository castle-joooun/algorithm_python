from collections import deque


def solution(key, lock):
    key = deque(key)

    def rotate(m):
        N = len(m)
        ret = [[0] * N for _ in range(N)]

        for r in range(N):
            for c in range(N):
                ret[c][N - 1 - r] = m[r][c]
        return ret

    # lock 반전
    for i in range(len(lock)):
        for j in range(len(lock)):
            if lock[i][j] == 1:
                lock[i][j] = 0
            else:
                lock[i][j] = 1
    locks = deque(lock)

    # 4방향으로 돌리기
    for _ in range(4):
        keys = rotate(key)
        down = deque(keys)
        up = deque(keys)

        # 밑으로 내리기
        for i in range(len(key) - 1):
            if i != 0:
                down.appendleft([0] * len(key))
                down.pop()

            # 오른쪽으로 밀기
            for j in range(len(key) - 1):
                right = deque(down)
                right[i] = deque(right[i])
                right[i].appendleft(0)
                right[i].pop()

                if right == locks:
                    return True

            # 왼쪽으로 밀기
            for j in range(len(key) - 1):
                left = down
                left[i] = deque(left)
                left[i].append(0)
                left[i].popleft()

                if left == locks:
                    return True

        # 위로 올리기
        for i in range(len(key) - 1):
            if i != 0:
                up.append([0] * len(key))
                up.popleft()

            # 오른쪽으로 밀기
            for j in range(len(key) - 1):
                right = up
                right[i] = deque(right[i])
                right[i].appendleft(0)
                right[i].pop()

                if right == locks:
                    return True

            # 왼쪽으로 밀기
            for j in range(len(key) - 1):
                left = up
                left[i] = deque(left[i])
                left[i].append(0)
                left[i].popleft()

                if left == locks:
                    return True

    return False


key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

print(solution(key, lock))