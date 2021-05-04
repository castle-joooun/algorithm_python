from itertools import combinations

n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]

chickens, houses = [], []

for i in range(n):
    for j in range(n):
        if data[i][j] == 2:
            chickens.append([i, j])
        elif data[i][j] == 1:
            houses.append([i, j])

candidates = list(combinations(chickens, m))


def get_sum(candidate):
    result = 0

    for hx, hy in houses:
        minimum = 1e9

        for cx, cy in candidate:
            minimum = min(minimum, abs(hx - cx) + abs(hy - cy))
        result += minimum

    return result


result = 1e9
for candidate in candidates:
    result = min(result, get_sum(candidate))

print(result)
