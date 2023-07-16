import sys

input = sys.stdin.readline


# n2
def two_sum(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if target == nums[i] + nums[j]:
                return True

    return False


# nlogn
def two_pointer(nums, target):
    nums.sort()
    i = 0
    j = len(nums) - 1

    while i < j:
        if nums[i] + nums[j] == target:
            return True

        if nums[i] + nums[j] > target:
            i += 1
        else:
            j -= 1
    return False


print(two_sum(nums=[2, 1, 5, 7], target=14))
print(two_pointer(nums=[2, 1, 5, 7], target=14))
