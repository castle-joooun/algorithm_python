d = input()

stack = []
result = ''

for x in d:
    if x == '(':
        stack.append(x)
        continue
    if x == ')':
        for i in range(len(stack) - 1, -1, -1):
            if stack[i] == '(':
                stack.pop()
                break
            else:
                result += stack.pop()

    if x.isdigit():
        result += x
    else:
        if x in ['+', '-']:
            while stack:
                check = stack.pop()
                if check != '(':
                    result += check
                else:
                    stack.append(check)
                    break
            stack.append(x)
        elif x in ['*', '/']:
            if stack:
                check = stack.pop()
                if check in ['+', '-']:
                    result += check
                else:
                    stack.append(check)
            stack.append(x)
result += stack.pop()
print(result)