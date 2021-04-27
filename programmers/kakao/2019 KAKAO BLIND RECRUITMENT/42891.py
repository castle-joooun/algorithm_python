import heapq


def solution(foods, k):
    if sum(foods) >= k:
        return -1

    q = []
    for i in range(len(foods)):
        heapq.heappush(q, (foods[i], i + 1))

    sum_value = 0
    previous = 0
    length = len(foods)

    while sum_value + ((q[0][0] - previous) * length) <= k:
        now = heapq.heappop(q)[0]

        sum_value += (now - previous) * length
        length -= 1
        previous = now

    result = sorted(q, key=lambda x: x[1])
    return result[(k - sum_value) % length][1]
