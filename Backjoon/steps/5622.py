s = input()
result = 0

for x in s:
  check = x.lower()

  if check in ['a', 'b', 'c']:
    result += 3
  if check in ['d', 'e', 'f']:
    result += 4
  if check in ['g', 'h', 'i']:
    result += 5
  if check in ['j', 'k', 'l']:
    result += 6
  if check in ['m', 'n', 'o']:
    result += 7
  if check in ['p', 'q', 'r', 's']:
    result += 8
  if check in ['t', 'u', 'v']:
    result += 9
  if check in ['w', 'x', 'y', 'z']:
    result += 10

print(result)