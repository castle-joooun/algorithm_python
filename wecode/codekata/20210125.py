def two_sum(nums, target):
  arr = []
  for i in range(len(nums)):
    for j in range(len(nums)):
      if nums[i] + nums[j] == target:
        arr.append(i)
        arr.append(j)
        return arr
