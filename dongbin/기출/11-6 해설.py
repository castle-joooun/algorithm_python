import heapq


def solution(foods, k):
    if sum(foods) <= k:
        return -1

    q = []
    for i in range(len(foods)):
        heapq.heappush(q, (foods[i], i + 1))

    sum_value = 0  # 먹기 위해 사용한 시간
    previous = 0  # 직전에 다 먹은 시간
    length = len(foods)

    # 먹기 위해 사용한 시간 + (현재의 음식 시간 - 이전 음식 시간) * 현재 음식 개수와 k 비교
    while sum_value + ((q[0][0] - previous) * length) <= k:
        now = heapq.heappop(q)[0]
        sum_value += (now - previous) * length
        length -= 1
        previous = now

    result = sorted(q, key=lambda x: x[1])
    return result[(k - sum_value) % length][1]


foods = [3, 1, 2]
k = 5
print(solution(foods, k))
