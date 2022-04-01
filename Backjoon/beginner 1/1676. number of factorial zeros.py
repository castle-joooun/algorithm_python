def factorial(num):
    if num in [0, 1]:
        return 1

    return num * factorial(num - 1)


check = list(str(factorial(int(input()))))[::-1]
count = 0
for x in check:
    if x == '0':
        count += 1
    else:
        break

print(count)
