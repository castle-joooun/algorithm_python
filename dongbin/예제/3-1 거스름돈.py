def solution(m):
    answer = 0

    coin = [500, 100, 50, 10]

    for x in coin:
        answer += m // x
        m %= x

    return answer


print(solution(1260))
