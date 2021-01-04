d = input()

stack = []
result = ''
for x in d:
    if x.isdigit():
        result += x
    elif x in ['*', '/']:
        while stack and stack[-1] in ['*', '/']:
            result += stack.pop()
        stack.append(x)
    elif x in ['+', '-']:
        while stack and stack[-1] != '(':
            result += stack.pop()
        stack.append(x)
    elif x == ')':
        while stack and stack[-1] != '(':
            result += stack.pop()
        stack.pop()
    else:
        stack.append(x)
while stack:
    result += stack.pop()

print(result)