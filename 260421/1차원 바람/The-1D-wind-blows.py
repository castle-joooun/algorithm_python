from collections import deque

n, m, q = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
winds = [(int(r), d) for r, d in [input().split() for _ in range(q)]]

# Please write your code here.
"""
Q번 실행, 그게 최대 N번 실행될 수 있으므로 QN,
그리고 배열을 재 정렬하면서 N번 실행될 수 있음, 그게 N개
즉, N^3임.
N,M,Q는 100이므로 100^3
"""

a = [deque(x) for x in a]
for r, oper in q:
    check = a[r - 1]

    if oper == 'L':
        check.appendleft(check.pop())
    else:
        check.append(check.popleft())

    is_up, is_down = True, True
    for i in range(1, r):
        up_index = r - i
        up_row = None
        if not (0 <= up_index < n):
            is_up = False
        else:
            up_row = a[up_index]
        down_index = r + i
        down_row = None
        if not (0 <= down_index < n):
            is_down = False
        else:
            down_row = a[down_index]
        for j in range(m):
            

            
    
    