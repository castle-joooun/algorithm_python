# def build(x, y, a, b):
#     # a는 구조물. 0 기둥, 1 보
#     # b는 건축/철거. 0 철거, 1 건축

#     # 설치하게 되는 종류
#     # 기둥은 바닥에 있거나 보의 한쪽 끝부분에 있거나 다른 기둥 위에 있어야 함
#     # 보는 한쪽 끝부분이 기둥위에 있거나 양쪽 끝 부분이 다른 보와 동시에 연결되어 있어야 함
#     if a == 0:
#         if b == 0:
#             # 위에 기둥이 있을 겅우
#             if data[y + 1][x] == 1:
#                 return False
#             # 위에 보라면
#             if data[y + 1][x] == 2:
#                 # 옆에 기둥이 없다면
#                 if (x + 1 <= n + 1 and data[y][x + 1] != 1) or (0 <= x - 1 and data[y][x - 1] != 1):
#                     return False
#                 # 옆이 보라면
#                 if x + 1 <= n + 1 and data[y + 1][x + 1] == 2:
#                     # 옆도 보이고
#                     pass
#         else:
#             pass
#     else:
#         if b == 0:
#             pass
#         else:
#             pass


def solution(n, build_frame):
    answer = []

    data = [[0] * (n + 1) for _ in range(n + 1)]
    for d in build_frame:
        x, y, a, b = d
        # if build(x, y, a, b):
        #     answer.append([x, y, a])

    return sorted(answer, key=lambda x: (x[0], x[1]))


print(solution(5, [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1], [
      3, 2, 1, 1]]) == [[1, 0, 0], [1, 1, 1], [2, 1, 0], [2, 2, 1], [3, 2, 1], [4, 2, 1], [5, 0, 0], [5, 1, 0]])
