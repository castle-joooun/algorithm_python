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
winds = deque(winds)


def check_same(origin, temp):
    for i in range(m):
        if origin[i] == temp[i]:
            return True

    return False


def move_value(oper, q):
    if oper == 'L':
        q.appendleft(q.pop())
    else:
        q.append(q.popleft())


def trans_wind(wind):
    if wind == 'L':
        return 'R'
    return 'L'


while winds:
    r, oper = winds.popleft()
    now_index = r - 1
    check = a[now_index]

    move_value(oper, check)

    up_oper = trans_wind(oper)
    for i in range(1, n):
        if 0 <= now_index - i < n:
            if check_same(a[now_index - i + 1], a[now_index - i]):
                move_value(up_oper, a[now_index - i])
                up_oper = trans_wind(up_oper)
            else:
                break
        else:
            break

    down_oper = trans_wind(oper)
    for i in range(1, n):
        if 0 <= now_index + i < n:
            if check_same(a[now_index + i - 1], a[now_index + i]):
                move_value(down_oper, a[now_index + i])
                down_oper = trans_wind(down_oper)
            else:
                break
        else:
            break

for x in a:
    print(' '.join(str(i) for i in x))