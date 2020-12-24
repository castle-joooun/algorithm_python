a, b = input().split()

new_a = ''
new_b = ''

for x in a:
  new_a = x + new_a
for x in b:
  new_b = x + new_b

new_a, new_b = int(new_a), int(new_b)
print(max(new_a, new_b))