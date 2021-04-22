def build(bo, pilar, check):
    x, y, a = check
    # 기둥일때
    if a == 0:
        if y == 0 or bo[y][x - 1] == 1 or bo[y][x] == 1 or pilar[y - 1][x] == 0:
            return True
    # 보일때
    else:
        if pilar[y - 1][x] == 0 or pilar[y - 1][x + 1] == 0 or (bo[y][x - 1] == 1 and bo[y][x + 1] == 1):
            return True
    return False


def delete(bo, pilar, check):
    x, y, a = check
    arr = [[[x, y + 1, 0], [x, y + 1, 1], [x - 1, y + 1, 1]],
           [[x, y, 0], [x + 1, y, 0], [x - 1, y, 1], [x + 1, y, 1]]]

    for data in arr[a]:
        if build(bo, pilar, data):
            continue
        else:
            # 지어지지 않음
            return False
    return True


def solution(n, build_frame):
    bo = [[-1] * (n + 1) for _ in range(n + 1)]
    pilar = [[-1] * (n + 1) for _ in range(n + 1)]
    answer = []

    for x, y, a, b in build_frame:
        check = [x, y, a]
        if b == 1:
            if build(bo, pilar, check):
                if a == 0:
                    pilar[y][x] = 0
                else:
                    bo[y][x] = 1
        else:
            if a == 0:
                pilar[y][x] = -1
            else:
                bo[y][x] = -1

            if delete(bo, pilar, check):
                # 지어짐 -> 문제x -> 원상복구
                if a == 0:
                    pilar[y][x] = 0
                else:
                    bo[y][x] = 1

    for i in range(n + 1):
        for j in range(n + 1):
            if bo[i][j] == 1:
                answer.append([j, i, 1])
            if pilar[i][j] == 0:
                answer.append([j, i, 1])

    return sorted(answer, key=lambda x: (x[0], x[1], x[2]))


print(solution(5, [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]))