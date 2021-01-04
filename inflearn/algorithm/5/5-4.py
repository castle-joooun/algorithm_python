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
check = []
i = 0
while i < len(d):
    if d[i] in ['+', '-', '*', '/']:
        j = i
        while d[j - 1].isdigit():
            check = [d[j - 1]] + check
            j -= 1
        if len(check) == 1:
            a, b = num.pop(), check.pop()
        elif len(check) >= 2:
            b = check.pop()
            a = check.pop()
        else:
            b = num.pop()
            a = num.pop()
        num.append(operate(int(a), int(b), d[i]))
    i += 1

print(num[0])