from collections import deque

n, t = map(int, input().split())
u = list(map(int, input().split()))
d = list(map(int, input().split()))

# Please write your code here.
q = deque(u + d)

for _ in range(t):
    q.appendleft(q.pop())

q = list(q)
print(' '.join(str(a) for a in q[:n]))
print(' '.join(str(a) for a in q[n:]))
    