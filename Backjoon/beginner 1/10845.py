import sys
from collections import deque

input = sys.stdin.readline

queue = deque()
for _ in range(int(input().strip())):
    order = input().split()
    if order[0] == 'push':
        queue.append(int(order[1]))
    elif order[0] == 'pop':
        if len(queue) > 0:
            print(queue.popleft())
        else:
            print(-1)
    elif order[0] == 'size':
        print(len(queue))
    elif order[0] == 'empty':
        print(int(len(queue) == 0))
    elif order[0] == 'front':
        if len(queue) > 0:
            print(queue[0])
        else:
            print(-1)
    elif order[0] == 'back':
        if len(queue) > 0:
            print(queue[-1])
        else:
            print(-1)
