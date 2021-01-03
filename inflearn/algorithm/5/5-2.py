d = input()

check = 0
result = 0
i = 0

while i < len(d):
    if i == len(d) - 1 and d[len(d) - 1] == ')':
        result += 1
        break

    if d[i] + d[i + 1] == '()':
        result += check
        i += 2
        continue

    if d[i] == '(':
        check += 1
    elif d[i] == ')':
        result += 1
        check -= 1

    i += 1

print(result)