def check_here(mid):
    cnt = 1
    here = d[0]
    for i in range(1, n):
        if d[i] - here >= mid:
            cnt += 1
            here = d[i]
    return cnt


n, c = map(int, input().split())
d = []

for _ in range(n):
    d.append(int(input()))

d.sort()
lt = 1
rt = max(d)
result = 0
while lt <= rt:
    mid = (lt + rt) // 2

    if check_here(mid) >= c:
        result = mid
        lt = mid + 1
    else:
        rt = mid - 1

print(result)