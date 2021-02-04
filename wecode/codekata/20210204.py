def top_k(nums, k):
  check = [0] * (max(nums) + 1)

  for num in nums:
    check[num] += 1

  result = []
  for i in range(k):
    idx = check.index(max(check))
    result.append(idx)
    check[idx] = 0

  return result
