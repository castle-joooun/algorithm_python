def solution(key, lock):
    n = len(key)
    m = len(lock)
    hole = []
    check = []
    x = 0
    y = 0

    for i in range(m):
        for j in range(m):
            if lock[i][j] == 0:
                hole.append((i, j))

    for _ in range(4):
        while x != n -1:
            while y != n -1:





key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]