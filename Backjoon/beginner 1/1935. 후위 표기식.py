n = int(input())
s = input()
value = [int(input()) for _ in range(n)]

stack = []

for x in s:
    if x.isalpha():
        stack.append(value[ord(x) - ord('A')])
    else:
        b = stack.pop()
        a = stack.pop()
        if x == '*':
            stack.append(a * b)
        elif x == '+':
            stack.append(a + b)
        elif x == '-':
            stack.append(a - b)
        elif x == '/':
            stack.append(a / b)

print(f'{stack.pop():.2f}')