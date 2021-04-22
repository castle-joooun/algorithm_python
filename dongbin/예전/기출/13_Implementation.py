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
# ex) m = 3, min_arr = 5 -> 5개 중에서 3개를 고르는 것
# (1,2,3), (1,2,4), (1,2,5) 이런식으로 값을 담음 -> 3! 값만큼 돌려야함
# 값을 담은것을 기반으로 최솟값의 index 들을 골라서 총합을 계산
# 계산한것들중 제일 작은값 return
ii = 0
while ii + 1 != m:
    check_chicken(0, m, min_arr, check)
    ii += 1

print(min(check))
