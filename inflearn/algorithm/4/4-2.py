k, n = map(int, input().split())
d = []
for _ in range(k):
    d.append(int(input()))

max_num = 0
lt = 1
rt = max(d)
while lt <= rt:
    mid = (lt + rt) // 2
    check = 0
    for x in d:
        check += x // mid

    if check >= n:
        max_num = max(max_num, mid)
        lt = mid + 1
    else:
        rt = mid - 1

print(max_num)