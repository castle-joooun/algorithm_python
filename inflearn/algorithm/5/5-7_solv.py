from collections import deque

need = input()
n = int(input())

for k in range(1, n + 1):
    d = input()
    queue = deque(need)

    for i in range(len(d)):
        if d[i] in queue:
            if d[i] == queue.popleft():
                continue
            else:
                print("#%d NO" % k)
                break
    else:
        if queue:
            print("#%d NO" % k)
        else:
            print("#%d YES" % k)