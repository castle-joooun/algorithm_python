a, b, c = map(int, input().split())

result = 0
if c - b != 0:
  result = (a // (c - b)) + 1
if result <= 0:
  print(-1)
else:
  print(result)