d = input()
stack = []
result = 0

for i in range(len(d)):
    if d[i] == '(':
        stack.append(d[i])
    else:
        stack.pop()
        if d[i - 1] == '(':
            result += len(stack)
        else:
            result += 1

print(result)