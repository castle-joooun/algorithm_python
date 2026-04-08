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
def block(x, y):
    block_1 = [
        [(0, 0), (0, 1), (1, 1)],  # 원본
        [(0, 0), (1, 0), (1, -1)],  # 90도
        [(0, 0), (0, -1), (-1, -1)],  # 180도
        [(0, 0), (-1, 0), (-1, 1)],  # 270도
    ]
    block_2 = [
        [(0,0),(1,0),(2,0)],   # 세로
        [(0,0),(0,1),(0,2)],   # 가로
    ]
    max_sum = 0

    for check in block_1:
        is_possible = True
        temp = 0
        for dx, dy in check:

            nx, ny = i + dx, j + dy
            if 0 <= nx < n and 0 <= ny < m:
                temp += grid[nx][ny]
            else:
                is_possible = False

            if is_possible:
                max_sum = max(max_sum, temp)

    for check in block_2:
        is_possible = True
        temp = 0
        for dx, dy in check:

            nx, ny = i + dx, j + dy
            if 0 <= nx < n and 0 <= ny < m:
                temp += grid[nx][ny]
            else:
                is_possible = False

            if is_possible:
                max_sum = max(max_sum, temp)

    return max_sum


for i in range(n):
    for j in range(m):
        answer = max(answer, block(i, j))

print(answer)

