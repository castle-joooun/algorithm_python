n = int(input())
d = []
l = []
result = 0

for _ in range(n):
    d.append(list(map(int, input().split())))

d = sorted(d, key=lambda x:(x[0], x[1]))
print(d)


def check(d, idx, result):
    # re = result + 1
    result.append(d[idx])
    re = []
    for i in range(idx, len(d)):
        if d[idx] != d[i]:
            if d[idx][0] <= d[i][0] and d[idx][1] <= d[i][0]:
                print(d[idx], '->', d[i], '|| result =', re)
                re.append(check(d, i, re))

    return re

# 모르겠담



for i in range(n):
    print('시작 ->', d[i], '|| result =', result)
    l.append(check(d, i, l))
    result = max(result, len(l))
    l = []
print(result)