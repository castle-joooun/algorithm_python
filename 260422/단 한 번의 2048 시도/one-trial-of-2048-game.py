from collections import deque

# Read 4x4 grid
grid = [list(map(int, input().split())) for _ in range(4)]

# Read direction
dir = input()

# Please write your code here.
"""
n은 최소 한번 움직이니까 시간복잡도는 초과되지 않음
다만 한번 이동시 4^2를 검사한다고 치면, n^2 정도 될듯

움직이는 방향에 맞춰 해당 행/열에 대한 temp,
0을 제외한 숫자를 정렬한 뒤, 붙은 행에 대해 같은 숫자가 있을 시 +.
이때 같은 숫자가 2 이상일 수 있음으로 움직이는 방향에 따른 우선순위 존재.
"""

for i in range(4):
    x, y = None, None
    temp = []
    temp2 = deque()
    for j in range(4):
        if dir == 'L':
            x, y = i, j
        elif dir == 'R':
            x, y = i, 3 - j
        elif dir == 'U':
            x, y = j, i
        else:
            x, y = 3 - j, i

        if grid[x][y] == 0:
            continue
        if len(temp2) > 0 and temp2[0] == grid[x][y]:
            temp.append(temp2.popleft() + grid[x][y])
            temp2 = deque([])
        else:
            if len(temp2) > 0:
                temp.append(temp2.popleft())
            temp2.append(grid[x][y])
    if temp2:
        temp += temp2
    temp += [0] * (4 - len(temp))
    if dir in ['R', 'D']:
        temp = temp[::-1]

    if dir in ['R', 'L']:
        grid[x] = temp
    elif dir == 'U':
        for k in range(4):
            grid[k][i] = temp[k]
    else:
        for k in range(4):
            grid[3 - k][i] = temp[k]

for x in grid:
    print(' '.join(str(i) for i in x))

