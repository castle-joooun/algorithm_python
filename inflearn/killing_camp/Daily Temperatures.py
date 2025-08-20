# https://leetcode.com/problems/daily-temperatures/description/
from typing import List


def dailyTemperatures(temperatures: List[int]) -> List[int]:
    queue = []
    answer = [0] * len(temperatures)

    for idx, temper in enumerate(temperatures):
        while len(queue) != 0:
            l_idx, l_temper = queue[-1]
            if l_temper < temper:
                answer[l_idx] = idx - l_idx
                queue.pop()
            else:
                break
        queue.append([idx, temper])

    return answer


print(dailyTemperatures([73,74,75,71,69,72,76,73]))