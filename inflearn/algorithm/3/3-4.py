n, m = map(int, input().split())
d = list(map(int, input().split()))
lt = 0
rt = 1
cnt = 0
check = d[0]
while True:
    if check < m:
        if rt < n:
            check += d[rt]
            rt += 1
        else:
            break
    elif check == m:
        cnt += 1
        check -= d[lt]
        lt += 1
    else:
        check -= d[lt]
        lt += 1

print(cnt)