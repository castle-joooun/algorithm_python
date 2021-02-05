def get_max_area(height):

  max_width = 0

  for i in range(len(height) - 1):
    for j in range(i + 1, len(height)):
      check_height = min(height[i], height[j])

      check_width = check_height * (j - i)
      max_width = max(check_width, max_width)
      
  return max_width
