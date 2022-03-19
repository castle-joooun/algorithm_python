import sys

input = sys.stdin.readline


for _ in range(int(input())):
    stack = []
    for x in input().strip():
        if x == ')':
            if len(stack) == 0:
                print('NO')
                break

            if stack[-1] == '(':
                stack.pop()
        else:
            stack.append(x)
    else:
        if len(stack) == 0:
            print('YES')
        else:
            print('NO')

