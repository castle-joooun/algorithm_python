from collections import deque

necessary = input()
n = int(input())

for i in range(1, n + 1):
    d = deque(list(input()))
    idx = 0

    print('#%d' % i, end=' ')

    while len(d) > 0:
        check = d.popleft()
        if check in necessary:
            if check != necessary[idx]:
                print('NO')
                break
            else:
                idx += 1
    else:
        print('YES' if idx == len(necessary) else 'NO')