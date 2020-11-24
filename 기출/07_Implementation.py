s = input()

left = s[:len(s) // 2]
right = s[len(s) // 2 : len(s)]
sum_l = 0
sum_r = 0

for x in left:
    sum_l += int(x)

for x in right:
    sum_r += int(x)

if sum_l == sum_r:
    print('LUCKY')
else:
    print('READY')
