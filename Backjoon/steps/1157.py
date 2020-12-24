s = input()
d = [0 for _ in range(ord('Z') + 1)]

for x in s:
  d[ord(x.upper())] += 1

max_num = d.index(max(d))

if d[max_num] in d[max_num + 1:]:
  print('?')
else:
  print(chr(max_num))