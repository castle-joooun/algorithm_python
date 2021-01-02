n, m = map(int, input().split())
d = list(map(int, input().split()))

d.sort()
lt = 0
rt = n - 1
while lt <= rt:
    mid = (lt + rt) // 2
    if d[mid] == m:
        print(mid + 1)
        break
    elif d[mid] > m:
        rt = mid - 1
    else:
        lt = mid + 1
