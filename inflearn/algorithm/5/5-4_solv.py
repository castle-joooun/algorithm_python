def operate(a, b, oper):
    if oper == '+':
        return a + b
    elif oper == '-':
        return a - b
    elif oper == '*':
        return a * b
    else:
        return a / b

d = input()

stack = []
for x in d:
    if x.isdecimal():
        stack.append(int(x))
    else:
        b, a = stack.pop(), stack.pop()
        stack.append(operate(a, b, x))

print(stack[0])