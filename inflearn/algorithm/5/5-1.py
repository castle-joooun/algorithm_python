n, m = map(int, input().split())

d = str(n)
check = 0
cnt = 0
while cnt != m:
    if check == len(d) - 1:
        d = d.replace(d[check], '', 1)
        cnt += 1
        check = 0
        continue

    if d[check] < d[check + 1]:
        d = d.replace(d[check], '', 1)
        cnt += 1
        check = 0
    else:
        check += 1

print(d)