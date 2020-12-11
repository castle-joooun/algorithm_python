n, m = map(int, input().split())
d = []
house = []
chicken = []
result = 0

for _ in range(n):
    d.append(list(map(int, input().split())))

for r in range(n):
    for c in range(n):
        if d[r][c] == 1:
            house.append((r, c))
        if d[r][c] == 2:
            chicken.append((r, c))

min_arr = [[] for _ in range(len(chicken))]
i = 0
for cr, cc in chicken:
    for hr, hc in house:
        min_arr[i].append(abs(cr - hr) + abs(cc - hc))
    i += 1

print(min_arr)


# m개일때 어떻게 값을 골라서 저장시킬껀지
def check_chicken(start, end, min, result):
    if start == end:
        return

    for i in range(start, end):
        result[i].append

        check_chicken(start + 1, end, min, result)
    return result


check = [[] for _ in range(m)]
check_chicken(0, m, min_arr, check)
