def two_sum(nums, target):
    brain = {}
    for i, x in enumerate(nums):
        brain[x] = i

    for i, x in enumerate(nums):
        check = target - x
        if check in brain and i != brain[check]:
            return True
    return False


print(two_sum([4, 1, 9, 7, 5, 3, 16], 14))
