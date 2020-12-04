def solution(n, build_frame):
    answer = []

    for i in range(len(build_frame)):
        x = build_frame[i][0]
        y = build_frame[i][1]
        # 1 = pillar, 0 = bo
        a = build_frame[i][2]
        # 1 = build, 0 = destroy
        b = build_frame[i][3]

        # 일단 기본 틀을 만듬
        # 그 다음에 조건에 맞춰 True, False 체크
        if b == 1:
            # 보가 세워질 수 잇는 경우인지 체크
            if a == 0:
                # 보는 한쪽끝부분이 기둥위에 있거나 또는 양족 끝 부분이 다른 보와 동시에 연결되어 있어야 함
                # 보는 x축이 +1까지 범위
                pass
            elif a == 1:
                # 기둥은 바닥위에 있거나 보의 한족 끝부분 위에 있거나 또는 다른 기둥 위에 있어야 함위
                # 기둥은 y축이 +1까지 범위
                pass
        elif b == 0:
            # 기둥, 보를 삭제해줌



    return answer