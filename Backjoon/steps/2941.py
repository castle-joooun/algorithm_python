s = input()
cro = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for x in cro:
  s = s.replace(x, '*')

print(len(s))