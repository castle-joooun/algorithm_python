# https://leetcode.com/problems/two-sum/
from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    for i, num_1 in enumerate(nums):
        for j, num_2 in enumerate(nums):
            if i == j:
                continue

            if num_1 + num_2 == target:
                return [i, j]


print(twoSum([2,7,11,15], 9))