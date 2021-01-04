def operate(a, b, oper):
    if oper == '+':
        result = a + b
    elif oper == '-':
        result = a - b
    elif oper == '*':
        result = a * b
    else:
        result = a / b
    return result

d = input()

num = []
i = 0
while len(d) > 0:
    if d[i] in ['+', '-', '*', '/']:
        j = i
        check = []
        while d[j - 1].isdigit():
            check.append(d[j - 1])
            j -= 1
        if len(check) == 1:
            a, b = num.pop(), check.pop()
        elif len(check) == 2:
            a, b = check
            check.clear()
        else:
            a, b = num
            num.clear()
        num.append(operate(a, b, d[i]))
    i += 1

print(num[0])