def more_than_half(nums):
  check = [0] * (max(nums) + 1)

  for i in range(len(nums)):
    check[nums[i]] += 1

  return check.index(max(check)) if max(check) > len(nums) // 2 else -1
