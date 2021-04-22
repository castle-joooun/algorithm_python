s = input()
alpha = []
sum = 0

for x in s:
    if ord('A') <= ord(x) <= ord('Z'):
        alpha.append(x)
    else:
        sum += int(x)

alpha.sort()

for x in alpha:
    print(x, end='')
print(sum)