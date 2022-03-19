import sys

input = sys.stdin.readline

stack = []
n = int(input())
sequence = [1]
check = [int(input()) for _ in range(n)]
index = 2
check_index = 0

result = ['+']
while len(stack) != n:
    if index > n:
        stack.append(sequence.pop())
        result.append('-')
        continue

    if len(sequence) > 0 and sequence[-1] == check[check_index]:
        stack.append(sequence.pop())
        check_index += 1
        result.append('-')
        continue

    sequence.append(index)
    index += 1
    result.append('+')

if stack == check:
    for x in result:
        print(x)
else:
    print('NO')
