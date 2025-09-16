from collections import deque


def solution(queue1, queue2):
    length = len(queue1)

    queue1 = deque(queue1)
    queue2 = deque(queue2)
    q1_sum = sum(queue1)
    q2_sum = sum(queue2)

    for i in range(length * 3):
        if q1_sum == q2_sum:
            return i

        if q1_sum < q2_sum:
            num = queue2.popleft()
            q2_sum -= num
            q1_sum += num
            queue1.append(num)
        else:
            num = queue1.popleft()
            q1_sum -= num
            q2_sum += num
            queue2.append(num)

    return -1


print(solution([1, 1, 1, 1], [1, 1, 7, 1]))



