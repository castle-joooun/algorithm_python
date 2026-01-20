# https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/description/
import sys
from typing import List
import heapq


def smallestRange(nums: List[List[int]]) -> List[int]:

    for i in range(len(nums)):
        nums[i] = [[val, i] for val in nums[i]]

    pq = []
    max_val = -sys.maxsize
    for i in range(len(nums)):
        heapq.heappush(pq, nums[i][0])
        max_val = max(max_val, nums[i][0][0])

    answer = [pq[0][0], max_val]
    index_list = [0] * len(nums)

    while True:
        min_val, idx = heapq.heappop(pq)
        index_list[idx] += 1

        if index_list[idx] == len(nums[idx]):
            break

        next_num = nums[idx][index_list[idx]]
        heapq.heappush(pq, next_num)
        max_val = max(max_val, next_num[0])

        if max_val - pq[0][0] < answer[1] - answer[0]:
            answer = [pq[0][0], max_val]

    return answer


print(smallestRange([[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]))
