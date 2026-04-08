n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
answer = 0


# Please write your code here.

# N이 최대가 200이니까 200*200 배열이라고 치고,
# 각 블럭을 대입을 해봐야 하니까 2개 블럭 * 회전 4개 -> 8개.
# 200^2 + 8 이니까 시간복잡도는 N^2

# 2중 for문으로 돌면서 각각 열에 왓을때
# 일단 블럭 체크로 보내고(2개의 메서드)
# 각 블럭 체크 메서드에서 회전 메서드로 보내서 각 좌표가 positive 한지 체크

# 그러고 난뒤 각 블럭에 해당되는 sum을 뽑으면 될듯.
# 뽑을때는 각 블럭에 해당되는 value를 더해주는 방식.

def rotate(points):
    # 90도 시계방향: (x, y) → (y, -x)
    rotated = [(y, -x) for x, y in points]

    # 양수 정규화
    min_x = min(x for x, y in rotated)
    min_y = min(y for x, y in rotated)

    return [(x - min_x, y - min_y) for x, y in rotated]


def block(x, y):
    point_1 = [(x, y), (x, y + 1), (x + 1, y + 1)]
    point_2 = [(x, y), (x + 1, y), (x + 2, y)]
    max_sum = 0

    for _ in range(4):
        is_possible = True
        temp = 0

        for dx, dy in point_1:
            nx, ny = i + dx, j + dy
            if 0 <= nx < n and 0 <= ny < m:
                temp += grid[nx][ny]
            else:
                is_possible = False
                break

        if is_possible:
            max_sum = max(max_sum, temp)

        point_1 = rotate(point_1)

    for _ in range(4):
        is_possible = True
        temp = 0

        for dx, dy in point_2:
            nx, ny = i + dx, j + dy
            if 0 <= nx < n and 0 <= ny < m:
                temp += grid[nx][ny]
            else:
                is_possible = False
                break

        if is_possible:
            max_sum = max(max_sum, temp)

        point_2 = rotate(point_2)

    return max_sum


for i in range(n):
    for j in range(m):
        answer = max(answer, block(i, j))

print(answer)

