from collections import deque

n, k = map(int, input().split())
queue = deque(list(map(int, input().split())))

while queue:
    for _ in range(k -1):
        queue.append(queue.popleft())
    queue.popleft()
    if len(queue) == 1:
        print(queue[0])
        queue.popleft()