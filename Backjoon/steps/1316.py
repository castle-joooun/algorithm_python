count = 0

for _ in range(int(input())):
  s = input()
  check = []
  before = ''
  for i in range(len(s)):
    if before == s[i]:
      continue
    if s[i] not in check:
      check.append(s[i])
      before = s[i]
    else:
      break
  else:
    count += 1

print(count)