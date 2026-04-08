n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

# n - 1까지 k가 커질 수 있음.
# 근데 k가 k^2 + (k + 1)^2만큼의 비용이고, 이 비용이 m을 넘으면 안되기 때문에
# 전체 m을 구하는게 필요할 듯.

# for k in range(n-1)만큼인데,
# if k^2 + (k + 1)^2 < total_m 기준으로 해야함. 넘으면 break

# 그러고 난뒤 마름모가 커지는 메서드를 만들어야 하는데..
# 0일때는 자기 자신,
# 1일때는 그 전 값의 상하좌우,
# 2일때도 그 전 값의 상하좌우. 이런식으로 커지면 될듯.

# 일단 구현해보자.

total_gold = sum([sum(row) for row in grid]) * m

point = {0: [(0, 0)]}
arrows = [(0, 1), (1, 0), (0, -1), (-1, 0)]
max_gold = 0
for k in range(n):
    if k != 0:
        temp = set(point[k - 1])
        for x, y in point[k - 1]:
            for dx, dy in arrows:
                temp.add((dx + x, dy + y))
        point[k] = list(temp)

    for i in range(n):
        for j in range(n):
            gold_count = 0
            for dx, dy in point[k]:
                nx, ny = dx + i, dy + j
                if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 1:
                    gold_count += 1

            if (k ** 2) + ((k + 1) ** 2) <= gold_count * m:
                max_gold = max(max_gold, gold_count)

print(max_gold)
