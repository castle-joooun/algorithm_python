def overlap(d):
    num = d[0]
    cnt = 1
    idx = 0
    for i in range(1, l):
        if d[0] == num:
            cnt += 1
        else:
            idx = i
            break
    return cnt, d[idx] - d[0]


l = int(input())
d = list(map(int, input().split()))
m = int(input())

while m > 0:
    d.sort()
    cnt, step = overlap(d)
    for i in range(cnt):
        if m - step >= 0:
            d[i] += step
            m -= step
        else:
            d[i] -= m
            m = 0
            break

d.sort()
print(d[-1] - d[0])