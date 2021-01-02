n, m = map(int, input().split())
d = list(map(int ,input().split()))

lt = 1
rt = sum(d)
minute = 0

while lt <= rt:
    mid = (lt + rt) // 2
    cnt = 1
    check = 0
    for x in d:
        if check + x > mid:
            cnt += 1
            check = x
        else:
            check += x

    if cnt <= m:
        minute = mid
        rt = mid - 1
    else:
        lt = mid + 1

print(minute)
