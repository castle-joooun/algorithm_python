"""
128. Longest Consecutive Sequence

https://leetcode.com/problems/longest-consecutive-sequence/
"""
from typing import List, Dict


def longestConsecutive(nums: List[int]) -> int:
    if not nums:
        return 0

    nums_dict: Dict = {x: 0 for x in nums}
    nums.sort()

    for x in nums:
        if x - 1 in nums_dict:
            result: int = 1 + nums_dict[x - 1]
        else:
            result: int = 1

        nums_dict[x] = result

    return max(nums_dict.values())


print(longestConsecutive(nums=[0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
print(longestConsecutive(nums=[100, 4, 200, 1, 3, 2]))
