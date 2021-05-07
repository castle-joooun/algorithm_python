def solution(gems):
    answer = [1, len(gems)]

    total_count = len(set(gems))
    minimum = len(gems)

    l, r = 0, 0

    while True:
        if 0 > r or r >= len(gems) or 0 > l or l >= len(gems):
            break

        buy = []
        if r == len(gems) - 1:
            buy = gems[l:]
        else:
            buy = gems[l: r]

        if total_count <= len(set(buy)):
            if minimum > len(buy):
                answer = [l + 1, r]
                minimum = len(buy)

            l += 1
            r = l
            continue

        if total_count > len(set(buy)):
            r += 1

    return answer


print(solution(["DIA", "EM", "EM", "RUB", "DIA"]))
