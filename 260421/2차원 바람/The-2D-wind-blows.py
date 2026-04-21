from collections import deque

n, m, q = map(int, input().split())

# Create 2D array for building state
a = [list(map(int, input().split())) for _ in range(n)]

# Process wind queries
winds = [tuple(map(int, input().split())) for _ in range(q)]

# Please write your code here.

"""
재정렬 nlogn
재정렬 -> 4번
copy_map -> n^2
q번 -> q
=> 100 ^ 3


winds의 값을 받아 첫/두번째의 row, col를 정렬하여
pop/append 하여 정렬 후 다시 슬라이스하여 값 치환,

copy_map 만들어서 해당되는 부위의 평균값을 얻음,
다 완료된 이후 치환.

이 과정을 q번 반복
"""

re_sort = deque()
for x1, y1, x2, y2 in winds:
    re_sort = deque(a[x1 - 1][y1 - 1:y2])
    for i in range(x1, x2):
        re_sort.append(a[i][y2 - 1])
    for i in range(y2 - 2, y1 - 2, -1):
        re_sort.append(a[x2 - 1][i])
    for i in range(x2 - 2, x1 - 1, -1):
        re_sort.append(a[i][y1 - 1])

    re_sort.appendleft(re_sort.pop())
    re_sort = list(re_sort)
    index = y2 - len(a[x1 - 1][:y1 - 1])
    a[x1 - 1] = a[x1 - 1][:y1 - 1] + re_sort[:index] + a[x1 - 1][y2:]
    for i in range(x1, x2):
        a[i][y2 - 1] = re_sort[index]
        index += 1
    for i in range(y2 - 2, y1 - 2, -1):
        a[x2 - 1][i] = re_sort[index]
        index += 1
    for i in range(x2 - 2, x1 - 1, -1):
        a[i][y1 - 1] = re_sort[index]
        index += 1

    copy_map = [
        x[::] for x in a
    ]

    for i in range(x1 - 1, x2):
        for j in range(y1 - 1, y2):
            temp_sum = a[i][j]
            count = 1
            for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                nx, ny = i + dx, j + dy
                if 0 <= nx < n and 0 <= ny < m:
                    temp_sum += a[nx][ny]
                    count += 1
            copy_map[i][j] = temp_sum // count

    a = copy_map

for x in a:
    print(' '.join(str(i) for i in x))
