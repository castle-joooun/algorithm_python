from collections import deque

n, t = map(int, input().split())

l = list(map(int, input().split()))
r = list(map(int, input().split()))
d = list(map(int, input().split()))

# Please write your code here.
q = deque(l + r + d)

for _ in range(t):
    q.appendleft(q.pop())

q = list(q)
print(' '.join(str(a) for a in q[:n]))
print(' '.join(str(a) for a in q[n:n * 2]))
print(' '.join(str(a) for a in q[n * 2:]))