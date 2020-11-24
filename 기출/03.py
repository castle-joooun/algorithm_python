s = input()
zero = 0
one = 0
before = ''

for x in s:
    if x == before:
        continue

    if x == '0':
        zero += 1
    else:
        one += 1
    before = x

if zero < one:
    print(zero)
else:
    print(one)