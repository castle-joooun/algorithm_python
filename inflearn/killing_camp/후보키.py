# https://school.programmers.co.kr/learn/courses/30/lessons/42890
from itertools import combinations


def solution(relation):
    col_len = len(relation[0])  # col length
    row_len = len(relation)  # row length

    # 속성 개수 별 모든 조합을 만들어서 후보키 적합성을 검사한다
    candidate_keys = []
    for length in range(1, col_len + 1):
        for cols in combinations(range(col_len), length):
            is_minimality = True
            row_set = set()

            # 최소성 검사
            for key in candidate_keys:
                if set(key).issubset(set(cols)):
                    is_minimality = False
                    break
            if not is_minimality:
                continue

            # 유일성 검사
            for r in range(row_len):
                row_str = ''
                for c in cols:
                    row_str += relation[r][c]
                row_set.add(row_str)

            if len(row_set) == row_len:
                candidate_keys.append(cols)

    answer = len(candidate_keys)
    return answer


print(solution([["100", "ryan", "music", "2"], ["200", "apeach", "math", "2"],
                ["300", "tube", "computer", "3"],
                ["400", "con", "computer", "4"], ["500", "muzi", "music", "3"],
                ["600", "apeach", "music", "2"]]))
