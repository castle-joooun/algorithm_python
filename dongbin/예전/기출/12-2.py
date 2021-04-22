def check(d, x, y, a):
    # 기둥이 없으려면
    # 위에 기둥이 없거나
    # 옆에 보가 있고, 그 옆에도 보가 있거나
    # 옆에 보가 있고, 그 밑에 기둥이 있거나

    # 보가 없으려면
    # 보 위에 기둥이 없거나
    # 옆에 보가 있고
        # 그 옆에도 보가 있을 때
            # 그 밑에
    pass


def check_success(n, answer, remove):
    answer.remove(remove)

    d = [[-1] * (n + 2) for _ in range(n + 2)]

    for i in range(len(answer)):
        x = answer[i][0]
        y = answer[i][1]
        a = answer[i][2]

        d[y][x] = a

    for i in range(len(answer)):
        x = answer[i][0]
        y = answer[i][1]
        a = answer[i][2]

        if a == 0:
            if not (y == 0 or d[y][x] == 1 or d[y - 1][x] == 0 or d[y][x - 1] == 1):
                answer.append(remove)
                return False
        elif a == 1:
            if not (d[y - 1][x] == 0 or d[y - 1][x + 1] == 0 or (d[y][x - 1] == 1 and d[y][x + 1] == 1)):
                answer.append(remove)
                return False

    return True


def solution(n, build_frame):
    answer = []

    # map
    d = [[-1] * (n + 2) for _ in range(n + 2)]

    for i in range(len(build_frame)):
        x = build_frame[i][0]
        y = build_frame[i][1]
        # 1 = bo, 0 = pillar
        a = build_frame[i][2]
        # 1 = build, 0 = destroy
        b = build_frame[i][3]

        # 일단 기본 틀을 만듬
        # 그 다음에 조건에 맞춰 True, False 체크
        if b == 1:
            # 보가 세워질 수 잇는 경우인지 체크
            if a == 0:
                # 기둥은 바닥위에 있거나 보의 한족 끝부분 위에 있거나 또는 다른 기둥 위에 있어야 함
                # 기둥은 y축이 +1까지 범위
                if y == 0 or d[y][x] == 1 or d[y - 1][x] == 0 or d[y][x - 1] == 1:
                    answer.append([x, y, a])
                    d[y][x] = a
            elif a == 1:
                # 보는 한쪽끝부분이 기둥위에 있거나 또는 양족 끝 부분이 다른 보와 동시에 연결되어 있어야 함
                # 보는 x축이 +1까지 범위
                if d[y - 1][x] == 0 or d[y - 1][x + 1] == 0 or (d[y][x - 1] == 1 and d[y][x + 1] == 1):
                    answer.append([x, y, a])
                    d[y][x] = a
        elif b == 0:
            # 기둥, 보를 삭제해줌
            if (a == 0 and d[y][x] == 0) or (a == 1 and d[y][x] == 1):
                if check_success(n, answer, [x, y, a]):
                    d[y][x] = -1

    return sorted(answer, key=lambda x: (x[0], x[1], x[2]))


print(solution(5, [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]))
