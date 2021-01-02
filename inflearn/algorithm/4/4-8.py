n, m = map(int, input().split())
d = list(map(int, input().split()))

cnt = 0
lt = 0
rt = n - 1
while lt <= rt:
    d.sort()
    if d[lt] + d[rt] <= m:
        cnt += 1
        lt += 1
        rt -= 1
    else:
        cnt += 1
        rt -= 1
print(cnt)