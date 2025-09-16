from typing import List


def trap(height: List[int]) -> int:
    left, right = 0, len(height) - 1
    max_left, max_right = height[left], height[right]

    answer = 0
    while left < right:
        if max_left <= max_right:
            left += 1
            if height[left] < max_left:
                answer += (max_left - height[left])
            else:
                max_left = height[left]
        else:
            right -= 1
            if height[right] < max_right:
                answer += (max_right - height[right])
            else:
                max_right = height[right]

    return answer


print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))


