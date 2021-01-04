from collections import deque

n, m = map(int, input().split())
d = deque(list(map(int, input().split())))

cnt = 0
while True:
    check = d.popleft()
    if check < max(d):
        d.append(check)
        if m > 0:
            m -= 1
        else:
            m = len(d) - 1
    else:
        cnt += 1
        if m > 0:
            m -= 1
        else:
            print(cnt)
            break
