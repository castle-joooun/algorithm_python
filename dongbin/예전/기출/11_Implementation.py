from collections import deque


def check(y, x, n, result):
    if y < 0 or y >= n or x < 0 or x >= n:
        print(result + 1)
        return True


# n x n
n = int(input())
# apple
k = int(input())

d = [[0] * n for i in range(n)]
for _ in range(k):
    i, j = map(int, input().split())
    d[i][j] = 1

a = int(input())
arrows = [[] for i in range(a)]
for i in range(a):
    sec, arrow = input().split()
    arrows[i].append(int(sec))
    arrows[i].append(arrow)

now_arrow = ['R', 'D', 'L', 'U']
now = 0
tails = deque([])
result = 0
tails.append((0, 0))
check_bool = True

for i in range(a + 1):
    if i != 0 and arrows[i - 1][1] != now_arrow[now]:
        if arrows[i - 1][1] == 'D':
            now += 1
        else:
            now -= 1

    if now == 4:
        now = 0
    elif now == -1:
        now = 3

    while arrows[i - 1][0] != result:
        result += 1

        if now_arrow[now] == 'R':
            y, x = tails.popleft()
            x += 1
            tails.append((y, x))
            if check(y, x, n, result):
                check_bool = False
                break
        elif now_arrow[now] == 'D':
            y, x = tails.popleft()
            y += 1
            tails.append((y, x))
            if check(y, x, n, result):
                check_bool = False
                break
        elif now_arrow[now] == 'L':
            y, x = tails.popleft()
            x -= 1
            tails.append((y, x))
            if check(y, x, n, result):
                check_bool = False
                break
        elif now_arrow[now] == 'U':
            y, x = tails.popleft()
            y -= 1
            tails.append((y, x))
            if check(y, x, n, result):
                check_bool = False
                break

    if check_bool:
        break

# 꼬리 늘어나서 부딪히면 끝나게 설정
